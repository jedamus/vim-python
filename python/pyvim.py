#!/usr/bin/env python
# encoding=utf-8

# created Montag, 31. Dezember 2012 07:57 (C) 2012-2019 by Leander Jedamus
# modifiziert Sonntag, 26. Mai 2019 12:30 von Leander Jedamus
# modifiziert Dienstag, 21. Mai 2019 16:45 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 10:30 von Leander Jedamus
# modifiziert Donnerstag, 02. Mai 2019 16:28 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 16:33 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 18:04 von Leander Jedamus
# modifiziert Mittwoch, 09. August 2017 22:49 von Leander Jedamus
# modifiziert Sonntag, 16. August 2015 19:17 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:00 von Leander Jedamus
# modifiziert Samstag, 06. April 2013 04:32 von Leander Jedamus
# modifiziert Montag, 11. März 2013 15:30 von Leander Jedamus
# modifiziert Montag, 25. Februar 2013 09:01 von Leander Jedamus
# modifiziert Sonntag, 24. Februar 2013 05:56 von Leander Jedamus
# modifiziert Samstag, 23. Februar 2013 18:16 von Leander Jedamus
# modifiziert Montag, 18. Februar 2013 13:39 von Leander Jedamus
# modifiziert Dienstag, 12. Februar 2013 16:13 von Leander Jedamus
# modifiziert Dienstag, 12. Februar 2013 12:49 von Leander Jedamus
# modified Montag, 28. Januar 2013 12:36 by Leander Jedamus
# modified Samstag, 05. Januar 2013 08:00 by Leander Jedamus
# modified Montag, 31. Dezember 2012 16:22 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:20 by Leander Jedamus

"""
  Das ist das Modul, daß die Hilfsfunktionen für die Arbeit
  in vim bereitstellt.
"""

import time
import re
import os
import sys
import inspect
import pwd
import gettext

try:
  import MySQLdb as mdb
  """ Die Werte werden erst dann geladen, wenn sie auch benötigt werden.  """
  www = ""
  email = ""
  package = ""
except ImportError:
  """
    Hier sollten Sie Ihre Default-Werte einsetzen!
    Vor allem, wenn Sie keine Datenbank betreiben wollen.
  """
  www = "www.jedamus-solutions.de"
  email = "ljedamus@web.de"
  package = "de.jedamus-solutions"

""" Das hier funktioniert nur in vim: """
import vim

""" Hier wird die englische oder deutsche Sprachunterstützung geladen: """
scriptname = "pyvim.py"
scriptpath = os.path.realpath(os.path.abspath(os.path.split( \
               inspect.getfile(inspect.currentframe()))[0]))
#scriptpath = os.path.join(os.environ['HOME'],"vim","python")
#for path in sys.path:
    #if(os.access(os.path.join(path,scriptname), os.F_OK)):
        #scriptpath = path
try:
    trans = gettext.translation(scriptname,os.path.join(scriptpath,"translate"))
    #trans.install(unicode=False)
    trans.install()
except IOError:
    """ Fallback, falls die Sprache nicht geladen werden konnte: """
    def _ (s):
        return s

""" Der Buffer: """
b = vim.current.buffer
#n = b.name
#i = os.getlogin()

""" Die ID des Benutzers ("leander"): """
i = pwd.getpwuid(os.geteuid())[0]

""" Der Username aus dem GECOS-Feld (siehe man 3 getpwnam) ("Leander Jedamus"):
"""
u = (pwd.getpwnam(i)[4].split(","))[0]

""" Der DateString: "Dienstag, 21. Mai 2019 12:48" """
dt = time.strftime("%A, %d. %B %Y %H:%M")

""" Das Jahr: "2019" """
y  = time.strftime("%Y")

def escape(str):
  """

    escape:

    :param str str
      Der String, der escaped werden soll.

    Hier wird der String str mit Escape-Zeichen versehen, falls in
    str ein \e drin steht.
  """
  return re.sub(r"\"","\\\"",str)

def sr(reg,str):
  """

    SetRegister:

    :param str reg:
      Das Register ("a"-"z"), das gesetzt werden soll.

    :param str str:
      Der String, der mit dem Register aufgerufen werden soll.
      Beispiele sind in den vim_(sprachkürzel)_enter.py-Dateien
      zu finden.

    Diese Funktion setzt das vi-Register reg auf den String str.
    Der String str wird dazu escaped (siehe Funktion escape(str)).
    Wenn das Register reg="a" ist, dann kann man das Register mit
    @a abrufen.
  """
  vim.command("let @{r:s}=\"{s:s}\"".format(r=reg,s=escape(str)))

def M(linenr,prefix="",suffix=""):
  """

    Modified:

    :param int linenr
      Gibt die Zeile an, in der der Kommentar mit der
      Modifikationszeit stehen soll.
    :param str prefix
      Gibt den String für ein Kommentar-Anfang an.
    :param str suffix
      Gibt den String für das Kommentar-Ende an.

    Hier wird geschaut, ob schon eine Zeile für das heutige Datum
    und den jetzigen User existiert. Wenn ja, wird nur die Zeit
    aktualisiert, ansonsten eine neue Zeile gesetzt.
  """
  b = vim.current.buffer
  tdt = time.strftime("%A, %d. %B %Y")
  ti  = time.strftime("%H:%M")
  line = b[linenr]
  if(re.match(".*" + tdt + ".*",line)):
    if(re.match(".*" + u + ".*",line)):
      b[linenr] = re.sub(r"(.*)\d{2}:\d{2}(.*)","\g<1>" + ti + "\g<2>",line)
    else:
      b[linenr:0] = [ prefix + m() + suffix ]
  else:
    b[linenr:0] = [ prefix + m() + suffix ]

def m():
    """

      modified:

      Diese Funktion gibt als String die Zeile zurück, in der das
      Modifikationsdatum und die Modifikationszeit als auch der User
      stehen.
      Um die jeweilige Sprache zu unterstützen, wird als Funktion
      _ (gettext) aufgerufen.
    """
    dt = time.strftime("%A, %d. %B %Y %H:%M")
    y  = time.strftime("%Y")
    return _("modified {dt:s} by {u:s}").format(dt=dt, u=u)

def b():
    """

      buffer:

      Gibt den aktuellen Buffer des vi zurück.
    """
    return vim.current.buffer

def cb():
    """

      created_by:

      Diese Funktion gibt als String die Zeile zurück, in der das
      Erzeugungsdatum und die Erzeugungszeit, das Copyright-Zeichen,
      das Jahr, in dem die Datei erzeugt wurde und der User, der die
      Datei als Erster geschrieben hat, steht.
      Um die jeweilige Sprache zu unterstützen, wird als Funktion
      _ (gettext) aufgerufen.
    """
    return _("created {dt:s} (C) {y:s} by {u:s}").format(dt=dt, y=y, u=u)

def c():
    """

      created:

      Diese Funktion gibt als String die Zeile zurück, in der das
      Erzeugungsdatum und die Erzeugungszeit steht.
      Um die jeweilige Sprache zu unterstützen, wird als Funktion
      _ (gettext) aufgerufen.
    """
    return _("created {dt:s}").format(dt=dt)

def by():
    """

      by:

      Diese Funktion gibt als String die Zeile zurück, in der das
      Copyright-Zeichen, das Jahr, in dem die Datei erzeugt wurde
      und der User, der die Datei als Erster geschrieben hat, steht.
      Um die jeweilige Sprache zu unterstützen, wird als Funktion
      _ (gettext) aufgerufen.

    """
    return _("(C) {y:s} by {u:s}").format(y=y, u=u)

def n():
    """

      name:

      Diese Funktion gibt den Namen der Datei zurück (mit Pfad).
    """
    return vim.current.buffer.name

def bn():
    """

      basename:

      Diese Funktion gibt nur den Namen der Datei zurück
      (also ohne Pfad).
    """
    return os.path.basename(n())

def db():
    """

      DataBase:

      Diese Funktion nimmt Kontakt mit der Datenbank auf.
      Es werden die Attribute email, www und package eingelesen 
      und gesetzt.
    """
    global email, www, package
    try:
        conn = mdb.connect(host='master',user='vim',passwd='ViM',db='vim');
        #cursor = conn.cursor()
        cursor = conn.cursor (mdb.cursors.DictCursor)
        cursor.execute("SELECT email, www, package FROM variables WHERE Id=%s",
                       (i,))
        # (email, www, package) = cursor.fetchone()
        row = cursor.fetchone()
        email   = row["email"]
        www     = row["www"]
        package = row["package"]
        return row
    except mdb.Error as e:
        print("Error {errno:d}: {error:s}".format(errno=e.args[0],
                                                  error=e.args[1]))

def em():
    """

      email:

      Hier wird die Email-Adresse des Benutzers zurückgegeben.
      Ist email anfangs leer, wird die Datenbank befragt und dort
      email gesetzt.
      Es sollte sowas wie "ljedamus@web.de" zurückgegeben werden.
      Das wird in HTML-Dateien benötigt (siehe "vim_html_neu.py").
    """
    if email == "":
      db()
    return email

def ww():
    """

      www:

      Hier wird die Web-Adresse des Benutzers zurückgegeben. Ist www
      anfangs leer, wird die Datenbank befragt und dort www gesetzt.
      Es sollte sowas wie "http://www.ljedamus.de/" zurückgegeben
      werden.
      Das wird in HTML-Dateien benötigt (siehe "vim_html_neu.py").
    """
    if www == "":
      db()
    return www

def pa():
    """

      package:

      Hier wird das Package des Benutzers zurückgegeben. Ist
      package anfangs leer, wird die Datenbank befragt und dort
      package gesetzt.
      Es sollte sowas wie "de.ljedamus" zurückgegeben werden.
      Das wird in Java-Dateien benötigt (siehe "vim_java_neu.py"):
      Heißt die Java-Datei beispielsweise
      /home/leander/tmp/de/ljedamus/mypack/pack1/mypack.java
      so wird folgendes gesetzt:
      package de.ljedamus.mypack.pack1;
    """
    if package == "":
      db()
    return package

def drs():
  """

    DeleteRegisters:

    Hier werden alle Register von a bis z zurückgesetzt.
  """
  vim.command("let @{r:s}=\"\"".format(r="a"))
  vim.command("let @{r:s}=\"\"".format(r="b"))
  vim.command("let @{r:s}=\"\"".format(r="c"))
  vim.command("let @{r:s}=\"\"".format(r="d"))
  vim.command("let @{r:s}=\"\"".format(r="e"))
  vim.command("let @{r:s}=\"\"".format(r="f"))
  vim.command("let @{r:s}=\"\"".format(r="g"))
  vim.command("let @{r:s}=\"\"".format(r="h"))
  vim.command("let @{r:s}=\"\"".format(r="i"))
  vim.command("let @{r:s}=\"\"".format(r="j"))
  vim.command("let @{r:s}=\"\"".format(r="k"))
  vim.command("let @{r:s}=\"\"".format(r="l"))
  vim.command("let @{r:s}=\"\"".format(r="m"))
  vim.command("let @{r:s}=\"\"".format(r="n"))
  vim.command("let @{r:s}=\"\"".format(r="o"))
  vim.command("let @{r:s}=\"\"".format(r="p"))
  vim.command("let @{r:s}=\"\"".format(r="q"))
  vim.command("let @{r:s}=\"\"".format(r="r"))
  vim.command("let @{r:s}=\"\"".format(r="s"))
  vim.command("let @{r:s}=\"\"".format(r="t"))
  vim.command("let @{r:s}=\"\"".format(r="u"))
  vim.command("let @{r:s}=\"\"".format(r="v"))
  vim.command("let @{r:s}=\"\"".format(r="w"))
  vim.command("let @{r:s}=\"\"".format(r="x"))
  vim.command("let @{r:s}=\"\"".format(r="y"))
  vim.command("let @{r:s}=\"\"".format(r="z"))

# vim:ai sw=2 sts=4 expandtab

