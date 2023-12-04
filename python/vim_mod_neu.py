#!/usr/bin/env python
# encoding=utf-8

# created Donnerstag, 10. August 2023 19:50 (C) 2023 by Leander Jedamus
# modifiziert Donnerstag, 10. August 2023 20:02 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.mod-Datei
  neu erzeugt werden soll.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import re
import vim
import pyvim as p

""" Hier wird der Dateiname ohne Endung .pas extrahiert. """
n = re.sub(r"(.*).mod","\g<1>",p.bn())

p.b()[0:0] = [ "MODULE {n:s};".format(n=n),
               "",
               "(* {cb:s} *)".format(cb=p.cb()),
	       "",
               "END {n:s}.".format(n=n),
               "",
	       "(* vim:set ai sw=2: *)"
             ]
vim.command("normal 4k4l")

# vim:ai sw=2 sts=4 expandtab

