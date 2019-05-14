#!/usr/bin/env python
# encoding=utf-8

# created Montag, 10. Dezember 2012 17:29 (C) 2012 by Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:42 von Leander Jedamus
# modifiziert Montag, 09. Juli 2018 10:31 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 17:52 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:00 von Leander Jedamus
# modifiziert Samstag, 23. Februar 2013 10:33 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:51 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:10 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:08 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:33 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:16 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:11 by Leander Jedamus
# modified Dienstag, 11. Dezember 2012 17:31 by Leander Jedamus
# modified Montag, 10. Dezember 2012 17:33 by Leander Jedamus

import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import vim
import pyvim as p

p.b()[0:0] = [ "/* -*- C -*- */",
	       "/* {n:s} */".format(n=p.bn()),
               "/* {cb:s} */".format(cb=p.cb()),
	       "",
	       "static const char* sccsid =",
	       "\"@(#) {n:s}, (C) {y:s} by {u:s}\";".format(n=p.bn(),y=p.y,
                                                            u=p.u),
	       "",
	       "/* vim:set cindent ai sw=2: */"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab

