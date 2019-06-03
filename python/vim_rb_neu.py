#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Donnerstag, 30. Mai 2019 14:30 (C) 2019 von Leander Jedamus
# modifiziert Freitag, 31. Mai 2019 11:13 von Leander Jedamus
# modifiziert Donnerstag, 30. Mai 2019 14:32 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.py- oder *.pyw-Datei
  neu erzeugt werden soll.

"""

from __future__ import print_function
import os
import sys
import re

sys.path.append(os.environ['HOME']+'/vim/python')

import vim
import pyvim as p

"""
  Das ist der Header einer Ruby-Datei. cb steht für created by
  (siehe pyvim.py).
"""
p.b()[0:0] = [ "#!/usr/bin/ruby -w",
               "# -*- coding: utf-8 -*-",
               "",
               "# {cb:s}".format(cb=p.cb()),
               "",
               'require "English"',
               "",
               "# vim:ai sw=2 sts=4 expandtab"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab

