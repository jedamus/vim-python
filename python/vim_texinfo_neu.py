#!/usr/bin/env python
# encoding=utf-8

# created Donnerstag, 10. August 2023 14:15 (C) 2023 by Leander Jedamus
# modifiziert Donnerstag, 10. August 2023 14:25 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.texinfo, *.txinfo oder
  *.texi-Datei neu erzeugt werden soll.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import vim
import pyvim as p

p.b()[0:0] = [
               "\input texinfo",
               "@c {cb:s}".format(cb=p.cb()),
	       "",
               "@include version.texinfo",
               "",
               "@settitle title",
               "",
	       "@c vim:set ai sw=2:"
             ]
vim.command("normal 4k3w")

# vim:ai sw=2 sts=4 expandtab

