#!/usr/bin/env python
# encoding=utf-8

# created Dienstag, 10. Oktober 2017 11:52 (C) 2017 by Leander Jedamus
# modifiziert Dienstag, 10. Oktober 2017 12:05 von Leander Jedamus

import re
import vim
import pyvim as p

n = re.sub(r"(.*).pas","\g<1>",p.bn())

p.b()[0:0] = [ "PROGRAM {n:s};".format(n=n),
               "",
               "(* {cb:s} *)".format(cb=p.cb()),
	       "",
               "BEGIN",
               "END.",
               "",
	       "(* vim:set ai sw=2: *)"
             ]
vim.command("normal 4k4l")

# vim:ai sw=2 sts=4 expandtab

