#!/usr/bin/env python
# encoding=utf-8

# erzeugt Montag, 25. Februar 2013 10:40 (C) 2013 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:00 von Leander Jedamus
# modifiziert Dienstag, 26. Februar 2013 09:19 von Leander Jedamus
# modifiziert Montag, 25. Februar 2013 18:52 von Leander Jedamus

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import sys
import re
import os
import gettext
import MySQLdb as mdb

from PyQt4.QtCore import (QStringList, Qt, QVariant, QString, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QHBoxLayout, QVBoxLayout,
                         QInputDialog, QLineEdit, QListWidget, QMessageBox,
                         QPushButton, QLabel, QTableView, QIcon)
from PyQt4.QtSql import (QSqlDatabase, QSqlTableModel)
import qrc_resources

scriptpath = os.path.abspath(os.path.dirname(sys.argv[0]))
try:
    trans = gettext.translation("edit_mysql_vim.py",os.path.join(scriptpath, \
                                                                 "translate"))
    trans.install(unicode=True)
except IOError:
    print("Fehler in gettext")
    sys.exit(-1)

ID      = 0
EMAIL   = 1
WWW     = 2
PACKAGE = 3

class DataDialog(QDialog):
    def __init__(self, name, table, parent=None):
        super(DataDialog, self).__init__(parent)

        self.name = name

        self.resize(600,300)

        self.model = QSqlTableModel(self)
        self.model.setTable(table)
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, QVariant(_("Id")))
        self.model.setHeaderData(EMAIL, Qt.Horizontal, QVariant(_("Email")))
        self.model.setHeaderData(WWW, Qt.Horizontal, QVariant(_("WWW")))
        self.model.setHeaderData(PACKAGE, Qt.Horizontal, QVariant(_("Package")))
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        #self.view.setColumnHidden(ID, True)
        #self.view.resizeColumnsToContents()

        addButton = QPushButton(_("&Add"))
        addButton.setIcon(QIcon(":/add.png"))
        deleteButton = QPushButton(_("&Delete"))
        deleteButton.setIcon(QIcon(":/delete.png"))
        okButton= QPushButton(_("&OK"))
        okButton.setIcon(QIcon(":/quit.png"))

        addButton.setFocusPolicy(Qt.NoFocus)
        deleteButton.setFocusPolicy(Qt.NoFocus)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(addButton)
        buttonLayout.addWidget(deleteButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.connect(addButton, SIGNAL("clicked()"), self.addRecord)
        self.connect(deleteButton, SIGNAL("clicked()"), self.deleteRecord)
        self.connect(okButton, SIGNAL("clicked()"), self.accept)

        self.setWindowTitle(name)

    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, EMAIL)
        self.view.setCurrentIndex(index)
        self.view.edit(index)

    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        self.model.removeRow(index.row())
        self.model.submitAll()

    def accept(self):
        QDialog.accept(self)

def createConnection():
    mdb = QSqlDatabase.addDatabase("QMYSQL")
    mdb.setHostName("localhost")
    mdb.setDatabaseName("vim")
    mdb.setUserName("vim")
    mdb.setPassword("ViM")
    if not mdb.open():
        QMessageBox.warning(None,"Edit MySQL Vim",
            QString("Database Error: %1").arg(mdb.lastError().text()))
        sys.exit(-1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/icon.png"))
    createConnection()
    form = DataDialog("Edit MySQL Vim","variables")
    form.exec_()

# vim:ai sw=2 sts=4 expandtab

