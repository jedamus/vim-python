autocmd BufNewFile *.pl py3file ~/vim/python/vim_pl_neu.py
autocmd BufWritePre *.pl py3file ~/vim/python/vim_pl_geaendert.py
autocmd BufEnter *.pl py3file ~/vim/python/vim_pl_enter.py
