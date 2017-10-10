autocmd BufNewFile *.pas py3file ~/vim/python/vim_pas_neu.py
autocmd BufWritePre *.pas py3file ~/vim/python/vim_pas_geaendert.py
autocmd BufEnter *.pas py3file ~/vim/python/vim_pas_enter.py
