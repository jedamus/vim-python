#!/usr/bin/env python
# encoding=utf-8

# created Freitag, 28. Dezember 2012 16:40 (C) 2012 by Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:49 von Leander Jedamus
# modifiziert Montag, 27. Mai 2019 12:03 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:43 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:01 von Leander Jedamus
# modifiziert Montag, 18. Februar 2013 13:09 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:52 by Leander Jedamus
# modified Montag, 28. Januar 2013 12:37 by Leander Jedamus
# modified Samstag, 19. Januar 2013 09:13 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:29 by Leander Jedamus
# modified Freitag, 28. Dezember 2012 16:41 by Leander Jedamus
# modified Freitag, 28. Dezember 2012 16:40 by Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.f-Datei
  geändert hat. Es wird nur ein Kommentar verändert oder neu
  gesetzt, wenn es zu dem aktuellen Datum keine Zeile für die
  Modifikation gibt.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import pyvim as p

p.M(1,"C ")

# vim:ai sw=2 sts=4 expandtab

