autocmd BufNewFile *.lisp pyfile ~/.vim/python/vim_lisp_neu.py
autocmd BufWritePre *.lisp pyfile ~/.vim/python/vim_lisp_geaendert.py
autocmd BufEnter *.lisp pyfile ~/.vim/python/vim_lisp_enter.py
