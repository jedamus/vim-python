#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 23. September 2017 12:57 (C) 2017 von Leander Jedamus
# modifiziert Freitag, 13. Juli 2018 13:14 von Leander Jedamus
# modifiziert Donnerstag, 12. Juli 2018 22:41 von Leander Jedamus
# modifiziert Donnerstag, 19. Oktober 2017 14:56 von Leander Jedamus
# modifiziert Samstag, 23. September 2017 16:37 von Leander Jedamus

import pyvim as p

p.drs()
#p.sr("a","iich bin in c.\n\e")
p.sr("i",":se ai\n:se nocindent\nA\nif () {\n};\ekA\n  \e:se cindent\nkwl")
p.sr("e",":se ai\n:se nocindent\n/};\n2s} \eAelse {\n};\ekA\n  \e:se cindent\nk$")
p.sr("l",":se ai\n:se nocindent\n/};\n2s} \eAelse if () {\n};\ekA\n  \e:se cindent\nk3wl")
p.sr("f",":se ai\n:se nocindent\nA\nfor (;;) {\n};\ekA\n  \e:se cindent\nkwl")
p.sr("s",":se ai\n:se nocindent\nA\nswitch () {\n};\ekA\n  case :\ncase :\ndefault:\ekkA\n         break;\ejA\n         break;\ejA\n         break;\e:se cindent\n6k^wl")
p.sr("d",":se ai\n:se nocindent\nA\ndo {\n} while ();\ekA\n  \e:se cindent\nj$h")
p.sr("w",":se ai\n:se nocindent\nA\nwhile () {\n};\ekA\n  \e:se cindent\nkwl")

# vim:ai sw=2 sts=4 expandtab

