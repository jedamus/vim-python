#!/usr/bin/env python
# encoding=utf-8

# created Dienstag, 10. Oktober 2017 12:01 (C) 2017 by Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:52 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 18:20 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:40 von Leander Jedamus
# modifiziert Dienstag, 10. Oktober 2017 12:02 von Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.pas-Datei
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

