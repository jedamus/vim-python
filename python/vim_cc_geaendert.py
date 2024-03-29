#!/usr/bin/env python
# encoding=utf-8

# created Montag, 10. Dezember 2012 17:24 (C) 2012 by Leander Jedamus
# modifiziert Montag, 27. Mai 2019 11:40 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:31 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:00 von Leander Jedamus
# modifiziert Montag, 18. Februar 2013 13:05 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:51 by Leander Jedamus
# modified Montag, 28. Januar 2013 12:37 by Leander Jedamus
# modified Montag, 28. Januar 2013 12:34 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:21 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:16 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:10 by Leander Jedamus
# modified Montag, 10. Dezember 2012 17:28 by Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.cc-, *.cpp-,
  *.c++-, *.cxx- oder *.C-Datei geändert hat. Es wird nur ein
  Kommentar verändert oder neu gesetzt, wenn es zu dem aktuellen
  Datum keine Zeile für die Modifikation gibt.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')
import pyvim as p

p.M(3,"// ")

# vim:ai sw=2 sts=4 expandtab

