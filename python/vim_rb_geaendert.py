#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Donnerstag, 30. Mai 2019 14:32 (C) 2019 von Leander Jedamus
# modifiziert Freitag, 31. Mai 2019 08:37 von Leander Jedamus
# modifiziert Donnerstag, 30. Mai 2019 14:33 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.rb-Datei
  geändert hat. Es wird nur ein Kommentar verändert oder neu
  gesetzt, wenn es zu dem aktuellen Datum keine Zeile für die
  Modifikation gibt.
"""

from __future__ import print_function
import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import pyvim as p

p.M(4,"# ")

# vim:ai sw=2 sts=4 expandtab

