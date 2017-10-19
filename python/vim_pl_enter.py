#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 23. September 2017 12:57 (C) 2017 von Leander Jedamus
# modifiziert Donnerstag, 19. Oktober 2017 14:56 von Leander Jedamus
# modifiziert Samstag, 07. Oktober 2017 18:04 von Leander Jedamus
# modifiziert Montag, 25. September 2017 20:30 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 23:46 von Leander Jedamus

import pyvim as p

p.drs()
#p.sr("a","iich bin in perl.\n\e")
p.sr("g","iuse Locale::gettext qw( gettext bindtextdomain textdomain bind_textdomain_codeset );\nuse POSIX;\nuse FindBin '$Bin';\nuse File::Spec;\n\nmy $domain = \"mycopy.pl\";\nbindtextdomain($domain,File::Spec->catfile($Bin,\"translate\"));\ntextdomain($domain);\nbind_textdomain_codeset($domain,\"UTF-8\");\nsub _ ($) { &gettext; }\n\e5k14l")

# if:
p.sr("i",":se ai\nA\nif () {\n};# if\ekA\n  \e^kwl")
# unless:
p.sr("u",":se ai\nA\nunless () {\n};# unless\ekA\n  \e^kwl")
# else:
p.sr("e",":se ai\n/;# \ns \eA\nelse {\n};# else\ekA\n  \e")
# elsif:
p.sr("l",":se ai\n/;# \ns \eA\nelsif () {\n};# elsif\ekA\n  \e^kwl")
# while
p.sr("w",":se ai\nA\nwhile () {\n};# while\ekA\n  \e^kwl")
# uNtil:
p.sr("n",":se ai\nA\nuntil () {\n};# until\ekA\n  \e^kwl")
# do while
p.sr("d",":se ai\nA\ndo {\n} while \ekA\n  \ej6l")
# do unTil
p.sr("t",":se ai\nA\ndo {\n} until \ekA\n  \ej6l")
# for
p.sr("f",":se ai\nA\nfor (my $;;) {\n};# for\ekA\n  \e^k3wl")
# fOreach
p.sr("o",":se ai\nA\nforeach my $ (@list) {\n};# foreach\ekA\n  \e^kw4l")

# vim:ai sw=2 sts=4 expandtab

