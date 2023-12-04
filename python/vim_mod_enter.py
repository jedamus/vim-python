#!/usr/bin/env python
# coding=utf-8

# erzeugt Donnerstag, 10. August 2023 21:22 (C) 2023 von Leander Jedamus
# modifiziert Donnerstag, 10. August 2023 21:25 von Leander Jedamus

"""
  Dieses Skript wird bei jedem Bufferwechsel in eine *.mod-
  Datei aufgerufen und setzt einige Register:

  @i (implementation): wandelt eine MODULE-Datei in eine IMPLEMENTATION MODULE um

  @n (function): function-Konstrukt

  @p (procedure): procedure-Kontrukt

  @c (case): case-Konstrukt

  @i (if): if-Konstrukt

  @e (else): else-Konstrukt

  @f (for): for-Konstrukt

  @o (for in): for-in-Konstrukt

  @w (while): while-Konstrukt
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import pyvim as p

p.drs()
# p.sr("a","iich bin in pascal.\n\e")

# fuNction
p.sr("n",":se ai\nA\nFUNCTION ;\n\nBEGIN\nEND;\ekA\n  \e^4k2w")
# Procedure
p.sr("p",":se ai\nA\nPROCEDURE ;\n\nBEGIN\nEND;\ekA\n  \e^4k2w")
# Case
p.sr("c",":se ai\nA\nCASE  OF\n:\n:\nELSE\nEND;\e^4k5l")
# If
p.sr("i",":se ai\nA\nIF THEN\nBEGIN\nEND;\ekA\n  \e^3kw3l")
# Else
p.sr("e",":se ai\n/;\ns \eA\nELSE\nBEGIN\nEND;\ekA\n  \e")
# For
p.sr("f",":se ai\nA\nFOR TO DO\nBEGIN\nEND;\ekA\n  \e^2kw")
# fOr in
p.sr("o",":se ai\nA\nFOR IN DO\nBEGIN\nEND;\ekA\n  \e^2kw")
# While
p.sr("w",":se ai\nA\nWHILE DO\nBEGIN\nEND;\ekA\n  \e^2kw")

# Implementation
p.sr("i",":1\n^iIMPLEMENTATION \e3j")

# vim:ai sw=2 sts=4 expandtab

