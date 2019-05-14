#!/usr/bin/env python
# encoding=utf-8

# created Freitag, 28. Dezember 2012 16:10 (C) 2012 by Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:42 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 17:55 von Leander Jedamus
# modifiziert Mittwoch, 13. September 2017 09:45 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:00 von Leander Jedamus
# modifiziert Samstag, 23. Februar 2013 10:35 von Leander Jedamus
# modifiziert Dienstag, 19. Februar 2013 10:40 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:52 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:10 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 16:22 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:25 by Leander Jedamus
# modified Freitag, 28. Dezember 2012 16:48 by Leander Jedamus
# modified Freitag, 28. Dezember 2012 16:25 by Leander Jedamus

import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import re
import vim
import pyvim as p

n = re.sub(r"(.*)\.cob","\g<1>",p.bn())
n = re.sub(r"\.","_",n)

p.b()[0:0] = [ "      * {c:s}".format(c=p.c()),
	       "      * {by:s}".format(by=p.by()),
	       "",
	       "       IDENTIFICATION DIVISION.",
	       "       PROGRAM-ID. {n:s}.".format(n=n),
               "       AUTHOR. {u:s}.".format(u=p.u),
               "       DATE-WRITTEN. {dt:s}.".format(dt=p.dt),
	       "       ",
	       "       ENVIRONMENT DIVISION.",
	       "       CONFIGURATION SECTION.",
	       "       ",
	       "       INPUT-OUTPUT SECTION.",
	       "       FILE-CONTROL.",
	       "           SELECT",
	       "           ASSIGN TO",
	       "           ORGANIZATION IS LINE SEQUENTIAL",
	       "           .",
	       "       ",
	       "       DATA DIVISION.",
	       "       FILE SECTION.",
	       "       FD .",
	       "           01 .",
	       "       ",
	       "       WORKING-STORAGE SECTION.",
	       "       ",
	       "       LOCAL-STORAGE SECTION.",
	       "       ",
	       "       LINKAGE SECTION.",
	       "       ",
	       "       SCREEN SECTION.",
	       "       ",
	       "      *",
	       "       PROCEDURE DIVISION.",
	       "       ",
	       "       STOP RUN.",
	       "       END PROGRAM {n:s}.".format(n=n),
	       "       ",
	       "      * vim:ai sw=4 sts=4 expandtab"
             ]
vim.command("normal 34k3w")

# vim:ai sw=2 sts=4 expandtab

