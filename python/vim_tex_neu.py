#!/usr/bin/env python
# encoding=utf-8

# created Montag, 10. Dezember 2012 16:13 (C) 2012 by Leander Jedamus
# modifiziert Montag, 27. Mai 2019 12:15 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:41 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 18:27 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:03 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:57 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:12 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:07 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:58 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:28 by Leander Jedamus
# modified Montag, 10. Dezember 2012 16:29 by Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.tex-Datei neu
  erzeugt werden soll.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import vim
import pyvim as p

p.b()[0:0] = [ "",
               "% {cb:s}".format(cb=p.cb()),
	       "",
	       "% vim:ai sw=2"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab

