autocmd BufNewFile *.js py3file ~/vim/python/vim_js_neu.py
autocmd BufWritePre *.js py3file ~/vim/python/vim_js_geaendert.py
autocmd BufEnter *.js py3file ~/vim/python/vim_js_enter.py
