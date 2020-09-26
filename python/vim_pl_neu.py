#!/usr/bin/env python
# encoding=utf-8

# created Mittwoch, 05. Dezember 2012 06:16 (C) 2012 by Leander Jedamus
# modifiziert Sonntag, 27. September 2020 00:52 von Leander Jedamus
# modifiziert Mittwoch, 22. Mai 2019 16:42 von Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:40 von Leander Jedamus
# modifiziert Montag, 16. Juli 2018 21:49 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 18:26 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:02 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:57 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:12 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:45 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:22 by Leander Jedamus
# modified Montag, 10. Dezember 2012 16:28 by Leander Jedamus
# modified Mittwoch, 05. Dezember 2012 06:18 by Leander Jedamus

"""
  Dieses Skript wird aufgerufen, wenn eine *.pl-Datei neu
  erzeugt werden soll.
"""

import os
import sys
sys.path.append(os.environ['HOME']+'/.vim/python')

import vim
import pyvim as p

"""
  Das ist der Header einer Perl-Datei. cb steht für created by
  (siehe pyvim.py).
"""
p.b()[0:0] = [ "#!/usr/bin/perl",
               "# -*- perl -*-",
               "# {cb:s}".format(cb=p.cb()),
	       "",
	       "use strict;",
	       "use warnings;",
	       "",
	       "# vim:ai sw=2"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab

