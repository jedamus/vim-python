#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Montag, 26. September 2022 15:21 (C) 2022 von Leander Jedamus
# modifiziert Montag, 26. September 2022 15:28 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.ipy-Datei
  neu erzeugt werden soll.

"""

import os
import sys
import re
sys.path.append(os.environ['HOME']+'/.vim/python')

import vim
import pyvim as p

command_line = 0
insert = []

"""
  Das ist der Header einer Python-Datei. cb steht für created by
  (siehe pyvim.py).
"""
kette = [ "#!/usr/bin/env ipython",
          "# coding=utf-8 -*- python -*-",
          "",
          "# {cb:s}".format(cb=p.cb()),
          "",
        ]

insert.extend(kette)
command_line = 5

kette = [ "",
          "# vim:ai sw=2 sts=4 expandtab",
        ]
insert.extend(kette)

p.b()[0:0] = insert
vim.command("normal " + ":1\n:{cl:d}\n".format(cl=command_line))

# vim:ai sw=2 sts=4 expandtab

