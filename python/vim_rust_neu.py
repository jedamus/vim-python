#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Mittwoch, 26. Oktober 2022 10:26 (C) 2022 von Leander Jedamus
# modifiziert Mittwoch, 26. Oktober 2022 10:34 von Leander Jedamus


"""
  Dieses Skript wird aufgerufen, wenn eine *.rs-Datei neu
  erzeugt werden soll.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import vim
import pyvim as p

p.b()[0:0] = [
               "// {cb:s}".format(cb=p.cb()),
	       "",
	       "// vim:ai sw=2"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab


# vim:ai sw=2 sts=4 expandtab

