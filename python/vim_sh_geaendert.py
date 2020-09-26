#!/usr/bin/env python
# encoding=utf-8

# created Mittwoch, 05. Dezember 2012 06:24 (C) 2012 by Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:54 von Leander Jedamus
# modifiziert Montag, 27. Mai 2019 12:16 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:41 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:02 von Leander Jedamus
# modifiziert Montag, 18. Februar 2013 13:17 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:57 by Leander Jedamus
# modified Montag, 28. Januar 2013 12:38 by Leander Jedamus
# modified Sonntag, 13. Januar 2013 19:20 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:58 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:18 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:13 by Leander Jedamus
# modified Montag, 10. Dezember 2012 16:29 by Leander Jedamus
# modified Mittwoch, 05. Dezember 2012 06:24 by Leander Jedamus

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

