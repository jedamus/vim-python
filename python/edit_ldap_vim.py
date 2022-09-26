#!/usr/bin/python
# coding=utf-8

# erzeugt Donnerstag, 14. März 2013 11:02 (C) 2013 von Leander Jedamus
# modified Donnerstag, 19. November 2020 09:06 by Leander Jedamus
# modifiziert Mittwoch, 29. Mai 2019 10:26 von Leander Jedamus
# modifiziert Dienstag, 28. Mai 2019 10:42 von Leander Jedamus
# modifiziert Dienstag, 19. März 2013 15:12 von Leander Jedamus
# modifiziert Montag, 18. März 2013 17:54 von Leander Jedamus
# modifiziert Sonntag, 17. März 2013 09:06 von Leander Jedamus
# modifiziert Samstag, 16. März 2013 18:56 von Leander Jedamus
# modifiziert Freitag, 15. März 2013 17:01 von Leander Jedamus
# modifiziert Donnerstag, 14. März 2013 17:15 von Leander Jedamus

# {{{1 Importe (open with "zo")
from __future__ import division
from __future__ import print_function
#from __future__ import unicode_literals
from future_builtins import *

import sys
import re
import os
import gettext
import ldap

from PyQt4.QtCore import (QStringList, Qt, SIGNAL, QTranslator, QLocale,
                          QByteArray)
from PyQt4.QtGui import (QApplication, QDialog, QHBoxLayout, QVBoxLayout,
                         QInputDialog, QLineEdit, QListWidget, QMessageBox,
                         QPushButton, QLabel, QIcon, QImage,QPixmap,
                         QErrorMessage, QFileDialog)
# }}}1

scriptpath   = os.path.abspath(os.path.dirname(sys.argv[0]))
imagespath   = os.path.join(scriptpath,"images")
qmPath       = "/usr/share/qt4/translations"
login_dn     = "cn=admin,dc=jedamus-solutions,dc=de"
ldap_host    = "ldap://localhost:389"
ldap_dn      = "ou=kottenheim,dc=jedamus-solutions,dc=de"
jpeg_dirname = "/home/leander/Bilder"
jpegPhoto    = "jpegPhoto"

try:
    trans = gettext.translation("edit_ldap_vim.py",os.path.join(scriptpath, 
                                                                "locale"))
    trans.install(unicode=True)
except IOError:
    #print("Fehler in gettext")
    #sys.exit(-1)
    def _ (s):
        return s

# {{{1 globale Variablen (open with "zo")
single_value = [
      # nis.schema
      "uidNumber", "gidNumber", "gecos", "homeDirectory", "loginShell",
      "shadowLastChange", "shadowMin", "shadowMax", "shadowWarning",
      "shadowInactive", "shadowExpire", "shadowFlag", "ipServicePort",
      "ipServiceProtocol", "ipProtocolNumber", "oncRpcNumber",
      "ipNetworkNumber", "ipNetmaskNumber", "nisMapEntry",
      # inetorgperson.schema
      "displayName", "employeeNumber", "preferredLanguage",
               ] 
not_editable = [
      "objectClass", jpegPhoto,
               ]

# }}}1

# {{{1 EditDialog (open with "zo")
class EditDialog(QDialog):
    def __init__(self, name, l, uid, new=False, parent=None):
        super(EditDialog, self).__init__(parent)

        self.name = name
        self.uid = uid
        self.l = l
        self.error = False
        self.image = None

        try:
            res = l.search_s(
                    "uid={l:s},{dn:s}".format(l=uid, dn=ldap_dn),
                    ldap.SCOPE_SUBTREE,
                    "objectclass=*",
                            )
            edit_form = []
            keys = res[0][1].keys()
            keys.sort()
            for key in keys:
                is_editable = True
                if key == jpegPhoto:
                    jpeg = res[0][1][key][0]
                    jpba = QByteArray.fromBase64(jpeg)
                    self.image = QImage.fromData(jpba, "JPG")
                for not_edit in not_editable:
                    if key == not_edit: is_editable = False
                edit_form.append((key+":", key, res[0][1][key], is_editable))

            frameLayout = QVBoxLayout()
            editLayout = QHBoxLayout()
            iconLayout = QHBoxLayout()
            self.iconLabel = QLabel()
            if self.image is not None:
                self.iconLabel.setPixmap(QPixmap.fromImage(self.image))
                buttonText = _("Change picture")
            else:
                buttonText = _("Insert picture")
            self.iconButton = QPushButton(buttonText)
            self.iconButton.setFocusPolicy(Qt.NoFocus)
            self.connect(self.iconButton, SIGNAL("clicked()"), self.editImage)
            iconLayout.addStretch()
            iconLayout.addWidget(self.iconLabel)
            iconLayout.addWidget(self.iconButton)
            iconLayout.addStretch()
            frameLayout.addLayout(iconLayout)

            width = 4
            rowLayout = []
            for i in range(width):
                rowLayout.append(QVBoxLayout())
                editLayout.addLayout(rowLayout[i])

            i = 0
            self.result = []
            for labeltext, key, text, is_editable in edit_form:
                if is_editable:
                    is_single = False
                    for single in single_value:
                        if key == single: is_single = True
                    if not is_single: text.append("")
                    for t in text:
                        leLayout = QHBoxLayout()
                        label = QLabel(labeltext)
                        edit  = QLineEdit(t)
                        leLayout.addWidget(label)
                        leLayout.addWidget(edit)
                        rowLayout[i].addLayout(leLayout)
                        i += 1
                        if i == width: i = 0
                        self.result.append((key, edit, True))
                else:
                    self.result.append((key, text, False))
            for i in range(width):
                rowLayout[i].addStretch()

            button2Layout = QHBoxLayout()
            button2Layout.addStretch()
            for text, slot, icon in ((_("Save"), self.close,
                                      "dialog-ok-apply.png"),
                                     (_("Cancel"), self.cancel,
                                      "dialog-cancel.png"),
                                    ):
                button = QPushButton(text)
                button.setFocusPolicy(Qt.NoFocus)
                if icon != "":
                    button.setIcon(QIcon(os.path.join(imagespath,icon)))
                button2Layout.addWidget(button)
                self.connect(button, SIGNAL("clicked()"), slot)
            button2Layout.addStretch()
            frameLayout.addLayout(editLayout)

            layout = QVBoxLayout()
            layout.addLayout(frameLayout)
            layout.addLayout(button2Layout)

            self.setLayout(layout)
            self.setWindowTitle(self.name)

        except ldap.LDAPError as e:
            error_msg(self, _("LDAP Error"), e)


    def close(self):
        res = []
        oldkey = ""
        for entry in self.result:
            (key, text, is_editable) = entry
            if key != oldkey:
                if oldkey != "":
                    res.append((oldkey, content))
                content = []
            if is_editable:
                t = str(text.text())
                if t != "":
                    content.append(t)
            else:
                for t in text:
                   content.append(t)
            oldkey = key
        if oldkey != "":
            res.append((oldkey, content))
        dn = "uid={l:s},{dn:s}".format(l=self.uid, dn=ldap_dn)
        try:
            if not self.error: self.l.delete_s(dn)
            self.l.add_s(dn, res)
            self.error = False
        except ldap.LDAPError as e:
            error_msg(self, _("LDAP Error"), e)
            self.error = True
        finally:
                if not self.error: QDialog.accept(self)

    def cancel(self):
        if self.error:
            resp = \
              QMessageBox().question(self,
                _("Object has been deleted"),
                _("Object has been deleted. Do you really want to continue?"),
                QMessageBox.Yes | QMessageBox.No)
            if resp == QMessageBox.Yes:
                QDialog.accept(self)
        else:        
            QDialog.accept(self)

    def editImage(self):
        global jpeg_dirname

        fileName = QFileDialog.getOpenFileName(self, _("JPEG-Filename"),
                                               jpeg_dirname,
                                               _("JPEG-Files (*.jpg)"))
        if fileName != "":
            fileName = str(fileName)
            (jpeg_dirname, ramsch) = os.path.split(fileName)
            if self.image is None:
                self.result.append((jpegPhoto, [""], False))
                self.image = ""
            for key, text, is_editable in self.result:
                if key == jpegPhoto:
                    string = open(fileName,"r").read()
                    byarr  = QByteArray(string)
                    by64   = byarr.toBase64()
                    text[0] = str(by64)
                    self.iconLabel.setPixmap(QPixmap.fromImage(
                      QImage.fromData(byarr, "JPG")))
                    self.iconButton.setText(_("Change picture"))
# }}}1

# {{{1 ListDialog (open with "zo")
class ListDialog(QDialog):
    def __init__(self, name, l, parent=None):
        super(ListDialog, self).__init__(parent)

        self.name = name
        self.l    = l

        self.listWidget = QListWidget()
        try:
            res = l.search_s(
                    ldap_dn,
                    ldap.SCOPE_SUBTREE,
                    "objectclass=*",
                            )
            n = 0
            for entry in res:
                if n != 0:
                    self.listWidget.addItem(entry[1]["uid"][0])
                    self.listWidget.setCurrentRow(0)
                n += 1

            editLayout = QHBoxLayout()
            editLayout.addWidget(self.listWidget)

            button1Layout = QVBoxLayout()
            for text, slot, icon in ((_("&Edit..."), self.edit, ""),
                                     (_("&New"), self.new, "add.png"),
                                     (_("&Remove"), self.remove, "delete.png"),
                                    ):
                button = QPushButton(text)
                button.setFocusPolicy(Qt.NoFocus)
                if icon != "":
                    button.setStyleSheet("QPushButton { text-align: left; }")
                    button.setIcon(QIcon(os.path.join(imagespath,icon)))
                button1Layout.addWidget(button)
                self.connect(button, SIGNAL("clicked()"), slot)
            button1Layout.addStretch()

            editLayout.addLayout(button1Layout)

            button2Layout = QHBoxLayout()
            button2Layout.addStretch()
            for text, slot, icon in ((_("Ok"), self.close,
                                     "dialog-ok-apply.png"),
                                    ):
                button = QPushButton(text)
                button.setFocusPolicy(Qt.NoFocus)
                if icon != "":
                    button.setIcon(QIcon(os.path.join(imagespath,icon)))
                button2Layout.addWidget(button)
                self.connect(button, SIGNAL("clicked()"), slot)
            button2Layout.addStretch()

            layout = QVBoxLayout()
            layout.addLayout(editLayout)
            layout.addLayout(button2Layout)

            self.setLayout(layout)
            self.setWindowTitle(self.name)

        except ldap.LDAPError as e:
            error_msg(self, _("LDAP Error"), e)

    def edit(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item is not None:
            editform = EditDialog(_("Edit entry"),self.l,item.text(),self)
            editform.exec_()
            if editform.error:
                self.listWidget.takeItem(row)

    def new(self):
        line = LineDialog(_("Enter Uid:"), False, self)
        line.exec_()
        dn = "uid={l:s},{dn:s}".format(l=line.text, dn=ldap_dn)
        try:
            self.l.add_s(dn,
             [
                ("objectClass",     ["developer", "posixAccount",
                                     "inetOrgPerson"]),
                ("uid",             [line.text]),
                ("uidNumber",       ["1002"]),
                ("gidNumber",       ["1002"]),
                ("sn",              ["testuser"]),
                ("telephoneNumber", ["+49-2651-41563"]),
                ("homeDirectory",   ["/home/testuser"]),
                ("loginShell",      ["/bin/zsh"]),
                ("userPassword",    ["test"]),
                ("cn",              ["testuser"]),
                ("mail",            ["testuser@web.de"]),
                ("title",           ["title"]),
                ("description",     ["description"]),
                ("devEmail",        ["testuser@kottenheim.ljedamus.de"]),
                ("devWWW",          ["http://www.testuser.de/"]),
                ("devPackage",      ["de.testuser"]),
             ]          )
            self.listWidget.addItem(line.text)
            self.listWidget.setCurrentRow(self.listWidget.count() - 1)
        except ldap.LDAPError as e:
            error_msg(self, _("LDAP Error"), e)

    def remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item is not None:
            resp = QMessageBox().question(
                     self, _("Remove uid {l:s}").format(l=item.text()),
                    _("Do you really want to remove uid={l:s} ?")
                       .format(l=item.text()),
                       QMessageBox.Yes | QMessageBox.No)
            if resp == QMessageBox.Yes:
                self.listWidget.takeItem(row)
                dn = "uid={l:s},{dn:s}".format(l=item.text(), dn=ldap_dn)
                try:
                    self.l.delete_s(dn)
                except ldap.LDAPError as e:
                    error_msg(self, _("LDAP Error"), e)

    def ok(self):
        QDialog.accept(self)
#}}}1

# {{{1 LineDialog (open with "zo")
class LineDialog(QDialog):
     def __init__(self, name, password=False, parent=None):
        super(LineDialog, self).__init__(parent)

        self.name = name
        self.text = ""

        self.edit = QLineEdit()
        if password: self.edit.setEchoMode(QLineEdit.Password)

        layout = QHBoxLayout()
        layout.addWidget(self.edit)
        button = QPushButton(_("Ok"))
        #button.setFocusPolicy(Qt.NoFocus)
        button.setIcon(QIcon(os.path.join(imagespath,"dialog-ok-apply.png")))
        layout.addWidget(button)
        self.connect(button, SIGNAL("clicked()"), self.ok)

        self.setLayout(layout)
        self.setWindowTitle(self.name)
        self.setMinimumSize(500,50)

     def ok(self):
        self.text = str(self.edit.text())
        QDialog.accept(self)
# }}}1

def error_msg(widget, header, e):
    errstr = ""
    if type(e.message) == dict:
        for key in e.message.keys():
            errstr += "<b>" + key + ":</b> " + e.message[key] + "<br>"
    else:
        errstr = e
    QMessageBox().warning(widget,header,errstr)

if __name__ == "__main__":
    l = ldap.initialize(ldap_host)
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(os.path.join(imagespath,
                                         "accessories-text-editor.png")))

    apptrans = QTranslator()
    apptrans.load("qt_" + QLocale.system().name(), qmPath)
    app.installTranslator(apptrans)

    input = LineDialog(_("password for %s: ") % login_dn, True)
    input.exec_()
    login_pw = input.text

    try:
        list = ListDialog(ldap_dn,l)
        l.simple_bind_s(login_dn, login_pw)
        list.exec_()
    except ldap.LDAPError as e:
        error_msg(list, _("Invalid credentials"), e)

    l.unbind()

# vim:ai sw=2 sts=4 expandtab

