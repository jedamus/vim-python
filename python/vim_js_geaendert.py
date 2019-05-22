#!/usr/bin/env python
# encoding=utf-8

# created Mittwoch, 12. Dezember 2012 07:41 (C) 2012 by Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 18:45 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:44 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:01 von Leander Jedamus
# modifiziert Montag, 18. Februar 2013 13:13 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:55 by Leander Jedamus
# modified Montag, 28. Januar 2013 12:38 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:39 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:17 by Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.js-Datei
  geändert hat. Es wird nur ein Kommentar verändert oder neu
  gesetzt, wenn es zu dem aktuellen Datum keine Zeile für die
  Modifikation gibt.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import pyvim as p

p.M(2,"// ")

# vim:ai sw=2 sts=4 expandtab

