source ~/.exrc
set softtabstop=4

set background=dark
syntax enable

set modeline
set modelines=2

"set mouse=a

"set fileencoding=utf-8
"set fileencoding=iso-8859-1

"set encoding=utf-8
"set encoding=iso-8859-1

" mapped F9 auf ctrl-]
map <F9> <C-]>

" Absatz formatieren
map <F3> gqap

" Zur letzten Position springen
autocmd BufReadPost * normal '"

set foldmethod=marker
" zo Open folded
" zc Close folded

if !exists("autocommands_loaded")
  let autocommands_loaded = 1

  " fuer python:
  source ~/vim/config/python.vim

  " fuer perl:
  source ~/vim/config/perl.vim

  " fuer pascal:
  source ~/vim/config/pascal.vim

  " fuer shell-skripte:
  source ~/vim/config/sh.vim

  " fuer c:
  source ~/vim/config/c.vim

  " fuer cc:
  source ~/vim/config/cc.vim

  " fuer cobol:
  source ~/vim/config/cobol.vim

  " fuer cascading stylesheets:
  source ~/vim/config/css.vim

  " fuer fortran:
  source ~/vim/config/fortran.vim

  " fuer h:
  source ~/vim/config/h.vim

  " fuer hh:
  source ~/vim/config/hh.vim

  " fuer html:
  source ~/vim/config/html.vim

  " fuer java:
  source ~/vim/config/java.vim

  " fuer javascript:
  source ~/vim/config/javascript.vim

  " fuer jsp:
  source ~/vim/config/jsp.vim

  " fuer lisp:
  source ~/vim/config/lisp.vim

  " fuer tex:
  source ~/vim/config/tex.vim

  " fuer Makefiles:
  source ~/vim/config/Makefile.vim

  " fuer lex oder flex:
  source ~/vim/config/lex.vim

  " fuer yacc oder bison:
  source ~/vim/config/yacc.vim
endif

