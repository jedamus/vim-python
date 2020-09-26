#!/usr/bin/env python
# encoding=utf-8

# created Mittwoch, 05. Dezember 2012 06:20 (C) 2012 by Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:52 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 16:40 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:40 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:02 von Leander Jedamus
# modifiziert Montag, 18. Februar 2013 13:16 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:56 by Leander Jedamus
# modified Montag, 28. Januar 2013 12:38 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:45 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:18 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:13 by Leander Jedamus
# modified Montag, 10. Dezember 2012 16:27 by Leander Jedamus
# modified Mittwoch, 05. Dezember 2012 06:20 by Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn sich eine *.pl-Datei
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

