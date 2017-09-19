#!/usr/bin/env python
# encoding=utf-8

# created Freitag, 28. Dezember 2012 16:33 (C) 2012 by Leander Jedamus
# modifiziert Dienstag, 19. September 2017 17:59 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:01 von Leander Jedamus
# modifiziert Samstag, 23. Februar 2013 10:36 von Leander Jedamus
# modifiziert Dienstag, 19. Februar 2013 10:34 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:53 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:11 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:30 by Leander Jedamus
# modified Freitag, 28. Dezember 2012 16:46 by Leander Jedamus

import re
import vim
import pyvim as p

n = re.sub(r"(.*)\.f\d{0,2}$","\g<1>",p.bn())
n = re.sub(r"\.","_",n)

p.b()[0:0] = [ "C {cb:s}".format(cb=p.cb()),
	       "       ",
	       "       PROGRAM {n:s}".format(n=n),
	       "       END PROGRAM {n:s}".format(n=n),
	       "       ",
	       "C vim:ai sw=4 expandtab"
             ]
vim.command("normal 4k2w")

# vim:ai sw=2 sts=4 expandtab

