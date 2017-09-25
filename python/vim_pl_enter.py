#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 23. September 2017 12:57 (C) 2017 von Leander Jedamus
# modifiziert Montag, 25. September 2017 20:30 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 23:46 von Leander Jedamus

import pyvim as p

p.drs()
#p.sr("a","iich bin in perl.\n")
p.sr("g","iuse Locale::gettext qw( gettext bindtextdomain textdomain bind_textdomain_codeset );\nuse POSIX;\nuse FindBin '$Bin';\nuse File::Spec;\n\nmy $domain = \"mycopy.pl\";\nbindtextdomain($domain,File::Spec->catfile($Bin,\"translate\"));\ntextdomain($domain);\nbind_textdomain_codeset($domain,\"UTF-8\");\nsub _ ($) { &gettext; }\n5k14l")

# if:
p.sr("i",":se ai\nAif () {\n};# ifkA\n  ^kwl")
# unless:
p.sr("u",":se ai\nAunless () {\n};# unlesskA\n  ^kwl")
# else:
p.sr("e",":se ai\n/;# \ns A\nelse {\n};# elsekA\n  ")
# elsif:
p.sr("l",":se ai\n/;# \ns A\nelsif () {\n};# elsifkA\n  ^kwl")
# while
p.sr("w",":se ai\nAwhile () {\n};# whilekA\n  ^kwl")
# uNtil:
p.sr("n",":se ai\nAuntil () {\n};# untilkA\n  ^kwl")
# do while
p.sr("d",":se ai\nAdo {\n} while kA\n  j6l")
# for
p.sr("f",":se ai\nAfor (my $;;) {\n};# forkA\n  ^k3wl")
# fOreach
p.sr("o",":se ai\nAforeach my $ (@list) {\n};# foreachkA\n  ^kw4l")

# vim:ai sw=2 sts=4 expandtab

