#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Mittwoch, 26. Oktober 2022 10:33 (C) 2022 von Leander Jedamus
# modifiziert Mittwoch, 26. Oktober 2022 10:34 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.rs-Datei geändert hat.
  Es wird nur ein Kommentar verändert oder neu gesetzt, wenn es zu dem
  aktuellen Datum keine Zeile für die Modifikation gibt.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')
import pyvim as p

p.M(1,"// ")

# vim:ai sw=2 sts=4 expandtab

