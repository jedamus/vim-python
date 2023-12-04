autocmd BufNewFile *.mod py3file ~/.vim/python/vim_mod_neu.py
autocmd BufWritePre *.mod py3file ~/.vim/python/vim_mod_geaendert.py
autocmd BufEnter *.mod py3file ~/.vim/python/vim_mod_enter.py
autocmd BufNewFile *.def py3file ~/.vim/python/vim_def_neu.py
autocmd BufWritePre *.def py3file ~/.vim/python/vim_def_geaendert.py
" autocmd BufEnter *.def py3file ~/.vim/python/vim_def_enter.py
