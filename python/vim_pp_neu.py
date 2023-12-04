#!/usr/bin/env python
# encoding=utf-8

# created Dienstag, 10. Oktober 2017 11:52 (C) 2017 by Leander Jedamus
# modifiziert Montag, 04. Dezember 2023 23:19 von Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:52 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 18:21 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:40 von Leander Jedamus
# modifiziert Dienstag, 10. Oktober 2017 12:05 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.pas-Datei neu
  erzeugt werden soll.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import re
import vim
import pyvim as p

""" Hier wird der Dateiname ohne Endung .pp extrahiert. """
n = re.sub(r"(.*).pp","\g<1>",p.bn())

p.b()[0:0] = [ "PROGRAM {n:s};".format(n=n),
               "",
               "(* {cb:s} *)".format(cb=p.cb()),
	       "",
               "BEGIN",
               "END.",
               "",
	       "(* vim:set ai sw=2: *)"
             ]
vim.command("normal 4k4l")

# vim:ai sw=2 sts=4 expandtab

