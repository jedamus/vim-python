#!/usr/bin/env python
# encoding=utf-8

# created Montag, 31. Dezember 2012 07:57 (C) 2012 by Leander Jedamus
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

import time
import re
import os
import sys
import inspect
import pwd
import gettext
#import MySQLdb as mdb
import ldap

import vim

scriptname = "pyvim.py"
scriptpath = os.path.realpath(os.path.abspath(os.path.split( \
               inspect.getfile(inspect.currentframe()))[0]))
dn="ou=kottenheim,dc=ljedamus,dc=de"

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
i = pwd.getpwuid(os.geteuid())[0]
try:
  l = ldap.open("marvin.fritz.box")
  res = l.search_s(
          "uid={i:s},{dn:s}".format(i=i, dn=dn),
          ldap.SCOPE_SUBTREE,
          "objectclass=*",
                  )
  u = res[0][1]["cn"][0]
  email = res[0][1]["devEmail"][0]
  www = res[0][1]["devWWW"][0]
  package = res[0][1]["devPackage"][0]

except ldap.LDAPError, e:
  print(e)

dt = time.strftime("%A, %d. %B %Y %H:%M")
y  = time.strftime("%Y")

def M(linenr,prefix="",suffix=""):
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
    dt = time.strftime("%A, %d. %B %Y %H:%M")
    y  = time.strftime("%Y")
    return _("modified {dt:s} by {u:s}").format(dt=dt, u=u)
def b():
    return vim.current.buffer
def cb():
    return _("created {dt:s} (C) {y:s} by {u:s}").format(dt=dt, y=y, u=u)
def c():
    return _("created {dt:s}").format(dt=dt)
def by():
    return _("(C) {y:s} by {u:s}").format(y=y, u=u)
def n():
    return vim.current.buffer.name
def bn():
    return os.path.basename(n())
def em():
    return email

def ww():
    return www

def pa():
    return package

# vim:ai sw=2 sts=4 expandtab

