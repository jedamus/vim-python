autocmd BufNewFile *.rb py3file ~/vim/python/vim_rb_neu.py
autocmd BufWritePre *.rb py3file ~/vim/python/vim_rb_geaendert.py
autocmd BufEnter *.rb py3file ~/vim/python/vim_rb_enter.py
