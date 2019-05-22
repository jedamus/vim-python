#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 23. September 2017 12:57 (C) 2017 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 18:59 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:45 von Leander Jedamus
# modifiziert Donnerstag, 19. Oktober 2017 14:56 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 16:40 von Leander Jedamus

"""
  Dieses Skript wird bei jedem Bufferwechsel in eine *.lisp-
  Datei aufgerufen und setzt momentan keine Register.
"""

import pyvim as p
import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

p.drs()
#p.sr("a","iich bin in lisp.\n\e")

# vim:ai sw=2 sts=4 expandtab

