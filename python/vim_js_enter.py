#!/usr/bin/env python
# coding=utf-8

# erzeugt Dienstag, 10. Oktober 2017 11:09 (C) 2017 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:44 von Leander Jedamus
# modifiziert Donnerstag, 19. Oktober 2017 14:55 von Leander Jedamus
# modifiziert Dienstag, 10. Oktober 2017 11:31 von Leander Jedamus

import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import pyvim as p

p.drs()
p.sr("a","iich bin in javascript.\n\e")
# if:
p.sr("i",":se ai\nA\nif () {\n};\ekA\n  \e^kwl")
# else:
p.sr("e",":se ai\n/;\ns \eA else {\n};\ekA\n  \e")
# elsif:
p.sr("l",":se ai\n/;\ns \eA else if () {\n};\ekA\n  \e^kwl")
# switch
p.sr("s",":se ai\nA\nswitch () {\n};// switch\ekA\n  case :\ncase :\ndefault:\e^2kA\n  break;\ejA\n  break;\ejA\n  break;\e7k2wl")
# while
p.sr("w",":se ai\nA\nwhile () {\n};// while\ekA\n  \e^kwl")
# do while
p.sr("d",":se ai\nA\ndo {\n} while ();\ekA\n  \ej8l")
# for
p.sr("f",":se ai\nA\nfor (;;) {\n};// for\ekA\n  \e^kwl")
# for in
p.sr("n",":se ai\nA\nfor ( in ) {\n};// for in\ekA\n  \e^kwl")

# vim:ai sw=2 sts=4 expandtab

