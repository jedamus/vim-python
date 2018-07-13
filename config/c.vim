autocmd BufNewFile *.c pyfile ~/vim/python/vim_c_neu.py
autocmd BufWritePre *.c pyfile ~/vim/python/vim_c_geaendert.py
autocmd BufEnter *.c pyfile ~/vim/python/vim_c_enter.py
