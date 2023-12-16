#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Samstag, 16. Dezember 2023 14:39 (C) 2023 von Leander Jedamus
# modifiziert Samstag, 16. Dezember 2023 14:49 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.php-Datei
  neu erzeugt werden soll.
"""

import os
import sys
import re
sys.path.append(os.environ['HOME']+'/.vim/python')

import vim
import pyvim as p

p.b()[0:0] = [ "<?php",
               "",
               "# {cb:s}".format(cb=p.cb()),
	       "",
	       "# vim:ai sw=2"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab

