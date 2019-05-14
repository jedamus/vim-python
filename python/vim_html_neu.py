#!/usr/bin/env python
# encoding=utf-8

# created Mittwoch, 12. Dezember 2012 07:43 (C) 2012 by Leander Jedamus
# modifiziert Dienstag, 14. Mai 2019 08:43 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 18:03 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:01 von Leander Jedamus
# modified Thursday, 20. November 2014 13:22 by Leander Jedamus
# modifiziert Dienstag, 12. März 2013 11:29 von Leander Jedamus
# modifiziert Montag, 11. März 2013 16:22 von Leander Jedamus
# modifiziert Montag, 25. Februar 2013 08:36 von Leander Jedamus
# modifiziert Samstag, 23. Februar 2013 17:44 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:54 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:11 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:37 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:17 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:12 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:09 by Leander Jedamus

import os
import sys
sys.path.append(os.environ['HOME']+'/vim/python')

import vim
#import pyvimldap as p
import pyvim as p

p.b()[0:0] = [ "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 " \
               "Transitional//EN\" " \
               "\"http://www.w3.org/TR/html4/loose.dtd\">",
	       "",
               "<!-- {cb:s} -->".format(cb=p.cb()),
	       "<html>",
	       "  <head>",
	       "    <meta http-equiv=\"content-type\" content=\"text/html; "
	              "charset=UTF-8\">",
	       "    <meta name=\"publisher\" content=\"{u:s}\">".format(u=p.u),
	       "    <meta name=\"copyright\" content=\"Copyright {y:s} by " \
                     "{u:s}\">"
	             .format(y=p.y,u=p.u),
               "    <meta name=\"generator\" content=\"vi\">",
               "    <meta name=\"publisher-email\" content=\"{em:s}\">".format(em=p.em()),
               "    <meta name=\"home_url\" content=\"{ww:s}\">".format(ww=p.ww()),
	       "    <title> </title>",
	       "  </head>",
	       "  <body>",
	       "  </body>",
	       "</html>",
	       "",
	       "<!-- vim:set ai sw=2: -->"
             ]
vim.command("normal 7k3wl")

# vim:ai sw=2 sts=4 expandtab

