#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 07. Oktober 2017 13:57 (C) 2017 von Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:50 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 18:36 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:43 von Leander Jedamus
# modifiziert Donnerstag, 19. Oktober 2017 14:55 von Leander Jedamus
# modifiziert Samstag, 07. Oktober 2017 17:48 von Leander Jedamus

"""
  Dieses Skript wird bei jedem Bufferwechsel in eine *.java-
  Datei aufgerufen und setzt einige Register:

  @i (if): if-Konstrukt

  @e (else): else-Konstrukt

  @s (switch): switch-Konstrukt

  @w (while): while-Konstrukt

  @d (do while): do-while-Konstrukt

  @f (for): for-Konstrukt

"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import pyvim as p

p.drs()
#p.sr("a","iich bin in java.\n\e")
# if:
p.sr("i",":se ai\nA\nif () {\n};// if\ekA\n  \e^kwl")
# else:
p.sr("e",":se ai\n/;// \ns \eA\nelse {\n};// else\ekA\n  \e")
# switch
p.sr("s",":se ai\nA\nswitch () {\n};// switch\ekA\n  case :\ncase :\ndefault:\e^2kA\n  break;\ejA\n  break;\ejA\n  break;\e7k2wl")
# while
p.sr("w",":se ai\nA\nwhile () {\n};// while\ekA\n  \e^kwl")
# do while
p.sr("d",":se ai\nA\ndo {\n} while ();\ekA\n  \ej8l")
# for
p.sr("f",":se ai\nA\nfor (;;) {\n};// for\ekA\n  \e^kwl")

# vim:ai sw=2 sts=4 expandtab

