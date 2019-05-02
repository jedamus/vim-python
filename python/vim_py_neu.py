#!/usr/bin/env python
# encoding=utf-8

# created Dienstag, 04. Dezember 2012 17:21 (C) 2012 by Leander Jedamus
# modifiziert Montag, 16. Juli 2018 16:00 von Leander Jedamus
# modifiziert Dienstag, 19. September 2017 18:26 von Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:02 von Leander Jedamus
# modifiziert Freitag, 26. Juni 2015 20:03 von Leander Jedamus
# modifiziert Montag, 11. März 2013 08:40 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:50 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:12 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:07 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:57 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 08:24 by Leander Jedamus
# modified Montag, 10. Dezember 2012 16:28 by Leander Jedamus
# modified Dienstag, 04. Dezember 2012 17:25 by Leander Jedamus

import vim
import pyvim as p

p.b()[0:0] = [ "#!/usr/bin/env python",
               "# coding=utf-8 -*- python -*-",
               "",
               "# {cb:s}".format(cb=p.cb()),
               "",
               "# vim:ai sw=2 sts=4 expandtab"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab

