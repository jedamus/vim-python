#!/usr/bin/env python
# encoding=utf-8

# created Mittwoch, 12. Dezember 2012 08:01 (C) 2012 by Leander Jedamus
# modifiziert Dienstag, 19. September 2017 18:12 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:01 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:56 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:12 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:42 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:17 by Leander Jedamus

import vim
import pyvim as p

p.b()[0:0] = [ "<%@ page language=\"java\" "
               "contentType=\"text/html; charset=UTF-8\"",
               "    errorPage=\"/errors/errorpage.jsp\" %>",
	       "",
               "<%-- {cb:s} --%>".format(cb=p.cb()),
	       "",
	       "<%-- vim:set ai sw=2: --%>"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab

