#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Freitag, 31. Mai 2019 08:24 (C) 2019 von Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:53 von Leander Jedamus
# modifiziert Freitag, 31. Mai 2019 09:31 von Leander Jedamus

from __future__ import print_function

"""
  Dieses Skript wird bei jedem Bufferwechsel in eine *.rb-
  Datei aufgerufen und setzt einige Register:

  @i (if): if-Konstrukt

  @e (else): else-Konstrukt

  @l (elsif): elsif-Konstrukt

  @u (unless): unless-Konstrukt

  @c (case): case-Konstrukt

  @f (for): for-Konstrukt

  @w (while): while-Konstrukt

  @n (until): until-Konstrukt

"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import pyvim as p

p.drs()
#p.sr("a","iich bin in ruby.\n\e")
p.sr("i","Aif  then\nend\ekA\n  \ek2l")
p.sr("e","/end\nielse\n\ekA\n  \e")
p.sr("l","/end\nielsif \n\ekA\n  \ek4l")
p.sr("u","Aunless  then\nend\ekA\n  \ek6l")
p.sr("c","Acase\nend\ekA\n  when  then\nwhen  then\nelse \e2kl")
p.sr("f","Afor  in \nend\ekA\n  \ek3l")
p.sr("w","Awhile  do\nend\ekA\n  \ek5l")
p.sr("n","Auntil  do\nend\ekA\n  \ek5l")

# vim:ai sw=2 sts=4 expandtab

