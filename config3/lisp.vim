autocmd BufNewFile *.lisp py3file ~/vim/python/vim_lisp_neu.py
autocmd BufWritePre *.lisp py3file ~/vim/python/vim_lisp_geaendert.py
autocmd BufEnter *.lisp py3file ~/vim/python/vim_lisp_enter.py
