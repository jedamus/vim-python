#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 23. September 2017 12:57 (C) 2017 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 23:46 von Leander Jedamus

import pyvim as p

p.drs()
#p.sr("a","iich bin in perl.\n")
p.sr("g","iuse Locale::gettext qw( gettext bindtextdomain textdomain bind_textdomain_codeset );\nuse POSIX;\nuse FindBin '$Bin';\nuse File::Spec;\n\nmy $domain = \"mycopy.pl\";\nbindtextdomain($domain,File::Spec->catfile($Bin,\"translate\"));\ntextdomain($domain);\nbind_textdomain_codeset($domain,\"UTF-8\");\nsub _ ($) { &gettext; }\n5k14l")

# if:
p.sr("i",":se noai\niif () {\n  \n};# if:se ai\n^2kwl")
# unless:
p.sr("u",":se noai\niunless () {\n  \n};# unless:se ai\n^2kwl")
# else:
p.sr("e",":se noai\n/;# \ns A\nelse {\n  \n};# else:se ai\n^k2l")
# elsif:
p.sr("l",":se noai\n/;# \ns A\nelsif () {\n  \n};# elsif:se ai\n^2kwl")
# while
p.sr("w",":se noai\niwhile () {\n  \n};# while:se ai\n^2kwl")
# uNtil:
p.sr("n",":se noai\niuntil () {\n  \n};# until:se ai\n^2kwl")
# do while
p.sr("d",":se noai\nido {\n  \n} while :se ai\n")
# for
p.sr("f",":se noai\nifor (;;) {\n  \n};# for:se ai\n^2kwl")
# fOreach
p.sr("o",":se noai\niforeach my $ (@list) {\n  \n};# foreach:se ai\n^2kw4l")

# vim:ai sw=2 sts=4 expandtab

