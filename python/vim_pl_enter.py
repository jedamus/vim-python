#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 23. September 2017 12:57 (C) 2017 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 16:36 von Leander Jedamus

import pyvim as p

p.drs()
#p.sr("a","iich bin in perl.\n")
p.sr("g","iuse Locale::gettext qw( gettext bindtextdomain textdomain bind_textdomain_codeset );\nuse POSIX;\nuse FindBin '$Bin';\nuse File::Spec;\n\nmy $domain = \"mycopy.pl\";\nbindtextdomain($domain,File::Spec->catfile($Bin,\"translate\"));\ntextdomain($domain);\nbind_textdomain_codeset($domain,\"UTF-8\");\nsub _ ($) { &gettext; }\n5k14l")

# vim:ai sw=2 sts=4 expandtab

