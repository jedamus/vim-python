#!/usr/bin/env python
# encoding=utf-8

# created Dienstag, 04. Dezember 2012 17:22 (C) 2012 by Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:53 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 16:38 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:41 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:02 von Leander Jedamus
# modifiziert Montag, 11. März 2013 08:41 von Leander Jedamus
# modifiziert Montag, 18. Februar 2013 13:40 von Leander Jedamus
# modified Montag, 28. Januar 2013 12:37 by Leander Jedamus
# modified Samstag, 05. Januar 2013 08:00 by Leander Jedamus
# modified Samstag, 05. Januar 2013 07:59 by Leander Jedamus
# modified Freitag, 04. Januar 2013 17:13 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:57 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:55 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:18 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:13 by Leander Jedamus
# modified Montag, 10. Dezember 2012 16:28 by Leander Jedamus
# modified Dienstag, 04. Dezember 2012 17:24 by Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.py- oder
  *.pyw-Datei geändert hat. Es wird nur ein Kommentar verändert
  oder neu gesetzt, wenn es zu dem aktuellen Datum keine Zeile
  für die Modifikation gibt.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import pyvim as p

p.M(4,"# ")

# vim:ai sw=2 sts=4 expandtab

