#!/usr/bin/env python
# coding=utf-8

# erzeugt Dienstag, 10. Oktober 2017 12:07 (C) 2017 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:39 von Leander Jedamus
# modifiziert Donnerstag, 19. Oktober 2017 14:54 von Leander Jedamus
# modifiziert Dienstag, 10. Oktober 2017 13:14 von Leander Jedamus

import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import pyvim as p

p.drs()
p.sr("a","iich bin in pascal.\n\e")

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

# Unit
p.sr("u",":1\n^cwUNIT\e4j^cwINTERFACE\n\nIMPLEMENTATION\n\e^2k")

# vim:ai sw=2 sts=4 expandtab

