#!/usr/bin/env python
# encoding=utf-8

# created Mittwoch, 05. Dezember 2012 06:23 (C) 2012 by Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:02 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:57 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:12 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:07 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:58 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:23 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:18 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:14 by Leander Jedamus
# modified Montag, 10. Dezember 2012 16:28 by Leander Jedamus
# modified Mittwoch, 05. Dezember 2012 06:24 by Leander Jedamus

import vim
import pyvim as p

p.b()[0:0] = [ "#!/bin/sh",
               "",
               "# " + p.cb(),
	       "",
	       "# vim:ai sw=2"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab

