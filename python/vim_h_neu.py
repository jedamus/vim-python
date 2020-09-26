#!/usr/bin/env python
# encoding=utf-8

# created Montag, 10. Dezember 2012 16:59 (C) 2012 by Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:50 von Leander Jedamus
# modifiziert Montag, 27. Mai 2019 11:49 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:43 von Leander Jedamus
# modifiziert Montag, 09. Juli 2018 10:36 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 18:00 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:01 von Leander Jedamus
# modifiziert Samstag, 23. Februar 2013 10:31 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:53 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:11 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:33 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:17 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:12 by Leander Jedamus
# modified Dienstag, 11. Dezember 2012 17:20 by Leander Jedamus
# modified Montag, 10. Dezember 2012 17:22 by Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.h-Datei neu
  erzeugt werden soll. Es werden unter anderem der Name
  der *.h-Datei, created by und eine Präprozessor-Direktive
  gesetzt, die dafür sorgt, daß die Header-Datei nur einmal
  eingelesen wird. Dazu wird der Dateiname ohne Pfad
  genommen und alle Punkte durch den Unterstrich ersetzt
  und der Dateiname groß geschrieben.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import re
import vim
import pyvim as p

n = p.bn()
n2 = re.sub(r"\.","_",n).upper()

p.b()[0:0] = [ "/* -*- C -*- */",
	       "/* {n:s} */".format(n=n),
               "/* {cb:s} */".format(cb=p.cb()),
	       "",
	       "#ifndef {n:s}".format(n=n2),
	       "#define {n:s} 1".format(n=n2),
	       "",
	       "#endif /* {n:s} */".format(n=n2),
	       "",
	       "/* vim:set cindent ai sw=2 */"
             ]

vim.command("normal 4k")

# vim:ai sw=2 sts=4 expandtab

