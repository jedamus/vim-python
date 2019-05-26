#!/usr/bin/env python
# encoding=utf-8

# created Montag, 31. Dezember 2012 07:57 (C) 2012 by Leander Jedamus
# modifiziert Sonntag, 26. Mai 2019 12:38 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:00 von Leander Jedamus
# modifiziert Samstag, 06. April 2013 04:33 von Leander Jedamus
# modifiziert Dienstag, 12. März 2013 11:28 von Leander Jedamus
# modifiziert Montag, 11. März 2013 16:21 von Leander Jedamus
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
  in vim bereitstellt (benutzt LDAP).
"""

import time
import re
import os
import sys
import inspect
import pwd
import gettext
#import MySQLdb as mdb
import ldap

dn="ou=kottenheim,dc=ljedamus,dc=de"

import vim

scriptname = "pyvim.py"
scriptpath = os.path.realpath(os.path.abspath(os.path.split( \
               inspect.getfile(inspect.currentframe()))[0]))

try:
    trans = gettext.translation(scriptname,os.path.join(scriptpath,"translate"))
    trans.install(unicode=False)
except IOError:
    def _ (s):
        return s

b = vim.current.buffer

www = ""
email = ""
package = ""

#i = os.getlogin()
""" Die ID des Benutzers ("leander"): """
i = pwd.getpwuid(os.geteuid())[0]
try:
  # l = ldap.initialize("ldap://marvin.fritz.box:389")
  l = ldap.initialize("ldap://localhost:389")
  res = l.search_s(
          "uid={i:s},{dn:s}".format(i=i, dn=dn),
          ldap.SCOPE_SUBTREE,
          "objectclass=*",
                  )
  """ Der Username aus dem LDAP-Feld cn ("Leander Jedamus"): """
  u = res[0][1]["cn"][0]
  email = res[0][1]["devEmail"][0]
  www = res[0][1]["devWWW"][0]
  package = res[0][1]["devPackage"][0]

except ldap.LDAPError as e:
  print(e)

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

def em():
    """

      email:

      Hier wird die Email-Adresse des Benutzers zurückgegeben.
      Es sollte sowas wie "ljedamus@web.de" zurückgegeben werden.
      Das wird in HTML-Dateien benötigt (siehe "vim_html_neu.py").
    """
    return email

def ww():
    """

      www:

      Hier wird die Web-Adresse des Benutzers zurückgegeben.
      Es sollte sowas wie "http://www.ljedamus.de/" zurückgegeben
      werden.
      Das wird in HTML-Dateien benötigt (siehe "vim_html_neu.py").
    """
    return www

def pa():
    """

      package:

      Hier wird das Package des Benutzers zurückgegeben.
      Es sollte sowas wie "de.ljedamus" zurückgegeben werden.
      Das wird in Java-Dateien benötigt (siehe "vim_java_neu.py"):
      Heißt die Java-Datei beispielsweise
      /home/leander/tmp/de/ljedamus/mypack/pack1/mypack.java
      so wird folgendes gesetzt:
      package de.ljedamus.mypack.pack1;
    """
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

