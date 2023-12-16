#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Samstag, 16. Dezember 2023 14:42 (C) 2023 von Leander Jedamus
# modifiziert Samstag, 16. Dezember 2023 14:42 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.sh-Datei
  geändert hat. Es wird nur ein Kommentar verändert oder neu
  gesetzt, wenn es zu dem aktuellen Datum keine Zeile für die
  Modifikation gibt.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import pyvim as p

p.M(3,"# ")

# vim:ai sw=2 sts=4 expandtab

