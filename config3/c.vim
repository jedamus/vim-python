autocmd BufNewFile *.c py3file ~/vim/python/vim_c_neu.py
autocmd BufWritePre *.c py3file ~/vim/python/vim_c_geaendert.py
autocmd BufEnter *.c py3file ~/vim/python/vim_c_enter.py
