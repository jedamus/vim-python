#!/usr/bin/env python
# encoding=utf-8

# created Montag, 10. Dezember 2012 16:59 (C) 2012 by Leander Jedamus
# modifiziert Freitag, 13. Juli 2018 13:42 von Leander Jedamus
# modifiziert Montag, 09. Juli 2018 10:35 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 18:00 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:01 von Leander Jedamus
# modifiziert Samstag, 23. Februar 2013 10:31 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:53 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:11 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:33 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:17 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:12 by Leander Jedamus
# modified Dienstag, 11. Dezember 2012 17:20 by Leander Jedamus
# modified Montag, 10. Dezember 2012 17:22 by Leander Jedamus

import re

import vim
import pyvim as p

n = p.bn()
n2 = re.sub(r"\.","_",n)
n3 = re.sub(r"\+","plus",n2).upper()

p.b()[0:0] = [ "// This may look like C code, but it is really -*- C++ -*-",
	       "// {n:s}".format(n=n),
               "// {cb:s}".format(cb=p.cb()),
	       "",
	       "#ifndef {n:s}".format(n=n3),
	       "#define {n:s} 1".format(n=n3),
	       "",
	       "#endif // {n:s}".format(n=n3),
	       "",
	       "// vim:cindent ai sw=2"
             ]

vim.command("normal 4k")

# vim:ai sw=2 sts=4 expandtab

