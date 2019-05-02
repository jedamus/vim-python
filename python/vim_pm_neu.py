#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Donnerstag, 02. Mai 2019 03:48 (C) 2019 von Leander Jedamus
# modifiziert Donnerstag, 02. Mai 2019 04:40 von Leander Jedamus

import re
import vim
import pyvim as p

n = re.sub(r"(.*).pm","\g<1>",p.bn())

p.b()[0:0] = [ "# -*- perl -*-",
               "# {cb:s}".format(cb=p.cb()),
	       "",
               "package {n:s};".format(n=n),
               "",
	       "use strict;",
	       "use warnings;",
               "use Exporter;",
               "our @ISA = qw(Exporter);",
               "our @EXPORT_OK = qw();",
	       "",
               "1;",
               "",
               "__END__",
               "",
               "=head1 NAME",
               "",
               "{n:s}".format(n=n),
               "",
               "=head1 SYNOPSIS",
               "",
               "=head1 DESCRIPTION",
               "",
	       "# vim:ai sw=2"
             ]
vim.command("normal 15k5wl")

# vim:ai sw=2 sts=4 expandtab

