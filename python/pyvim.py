#!/usr/bin/env python
# encoding=utf-8

# created Montag, 31. Dezember 2012 07:57 (C) 2012 by Leander Jedamus
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

import time
import re
import os
import sys
import inspect
import pwd
import gettext
import MySQLdb as mdb

import vim

scriptname = "pyvim.py"
scriptpath = os.path.realpath(os.path.abspath(os.path.split( \
               inspect.getfile(inspect.currentframe()))[0]))
#scriptpath = os.path.join(os.environ['HOME'],".vim","python")
#for path in sys.path:
    #if(os.access(os.path.join(path,scriptname), os.F_OK)):
        #scriptpath = path
try:
    trans = gettext.translation(scriptname,os.path.join(scriptpath,"translate"))
    #trans.install(unicode=False)
    trans.install()
except IOError:
    def _ (s):
        return s

b = vim.current.buffer
#n = b.name
#i = os.getlogin()
i = pwd.getpwuid(os.geteuid())[0]
u = (pwd.getpwnam(i)[4].split(","))[0]

dt = time.strftime("%A, %d. %B %Y %H:%M")
y  = time.strftime("%Y")

www = "www.ljedamus.de"
email = "ljedamus@testemail.com"
package = "de.ljedamus"

www = ""
email = ""
package = ""

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
def db():
    global email, www, package
    try:
        conn = mdb.connect('192.168.2.109','vim','ViM','vim');
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
    if email == "":
      db()
    return email

def ww():
    if www == "":
      db()
    return www

def pa():
    if package == "":
      db()
    return package

# vim:ai sw=2 sts=4 expandtab

