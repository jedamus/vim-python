#!/usr/bin/env python
# encoding=utf-8

# created Mittwoch, 12. Dezember 2012 07:35 (C) 2012 by Leander Jedamus
# modifiziert Sonntag, 26. Mai 2019 11:53 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 18:32 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:44 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 14:04 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 22:55 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:01 von Leander Jedamus
# modified Thursday, 20. November 2014 13:25 by Leander Jedamus
# modifiziert Dienstag, 12. März 2013 11:26 von Leander Jedamus
# modifiziert Sonntag, 24. Februar 2013 05:58 von Leander Jedamus
# modifiziert Samstag, 23. Februar 2013 11:37 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:55 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:11 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 16:37 by Leander Jedamus
# modified Montag, 31. Dezember 2012 16:28 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:38 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:17 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:12 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 07:37 by Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.java-Datei neu
  erzeugt werden soll.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

use_ldap = False

import re
import os
import vim
if use_ldap:
  import pyvimldap as p
else:
  import pyvim as p

""" Hier kommt der package-Prefix hinein: """
d=p.pa()

""" Hier wird der Dateiname ohne Endung .java extrahiert. """
n = re.sub(r"(.*).java","\g<1>",p.bn())

""" Hier wird der Pfad zur Java-Datei untersucht: """
path = os.path.split(p.n())[0]

""" Hier wird daraus der package-Name gebildet: """
packpath = re.sub(r"[/\\]",".",path)

""" Hier wird der package-Name erst ab dem package-Prefix gebildet """
package = re.sub(r".*\.{d:s}\.(.*)$".format(d=d),"{d:s}.\g<1>".format(d=d),
                 packpath)

p.b()[0:0] = [ "",
               "// {cb:s}".format(cb=p.cb()),
	       "",
	       "package {package:s};".format(package=package),
	       "",
	       "/**",
	       "  @author {u:s}".format(u=p.u),
	       "*/",
	       "public class {n:s}".format(n=n),
	       "{",
	       "  ",
	       "}}; // class {n:s}".format(n=n),
	       "",
	       "// vim:ai sw=2"
             ]
vim.command("normal 4kl")

# vim:ai sw=2 sts=4 expandtab

