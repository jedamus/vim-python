#!/usr/bin/env python
# encoding=utf-8

# created Donnerstag, 10. August 2023 19:52 (C) 2023 by Leander Jedamus
# modifiziert Donnerstag, 10. August 2023 20:06 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.def-Datei
  geändert hat. Es wird nur ein Kommentar verändert oder neu
  gesetzt, wenn es zu dem aktuellen Datum keine Zeile für die
  Modifikation gibt.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import pyvim as p

p.M(3,"(* "," *)")

# vim:ai sw=2 sts=4 expandtab

