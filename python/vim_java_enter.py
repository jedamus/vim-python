#!/usr/bin/env python
# coding=utf-8

# erzeugt Samstag, 07. Oktober 2017 13:57 (C) 2017 von Leander Jedamus
# modifiziert Samstag, 07. Oktober 2017 17:48 von Leander Jedamus

import pyvim as p

p.drs()
p.sr("a","iich bin in java.\n")
# if:
p.sr("i",":se ai\nA\nif () {\n};// ifkA\n  ^kwl")
# else:
p.sr("e",":se ai\n/;// \ns A\nelse {\n};// elsekA\n  ")
# switch
p.sr("s",":se ai\nA\nswitch () {\n};// switchkA\n  case :\ncase :\ndefault:^2kA\n  break;jA\n  break;jA\n  break;7k2wl")
# while
p.sr("w",":se ai\nA\nwhile () {\n};// whilekA\n  ^kwl")
# do while
p.sr("d",":se ai\nA\ndo {\n} while ();kA\n  j8l")
# for
p.sr("f",":se ai\nA\nfor (;;) {\n};// forkA\n  ^kwl")

# vim:ai sw=2 sts=4 expandtab

