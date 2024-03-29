#!/usr/bin/env sh

# erzeugt Montag, 14. Dezember 2020 14:29 (C) 2020 von Leander Jedamus
# modifiziert Samstag, 19. März 2022 16:58 von 
# modifiziert Sonntag, 27. Dezember 2020 18:00 von Leander Jedamus
# modifiziert Mittwoch, 23. Dezember 2020 10:08 von Leander Jedamus
# modifiziert Dienstag, 15. Dezember 2020 10:48 von Leander Jedamus
# modifiziert Montag, 14. Dezember 2020 23:42 von Leander Jedamus

vim=$HOME/.vim
CH=pyvim

cp -vp $vim/vimrc2 $HOME/.vimrc
cp -vp $vim/.exrc $HOME

cd $vim/python

if [ -z $3 ]; then
  if [ -f ${CH}.modify_me ]; then
    read -p "What is your email-address (ljedamus@web.de): " email
    echo "setting your email-address to $email"
    echo ""

    read -p "What is your WWW-address (http://www.jedamus-solutions.de/): " www
    echo "setting your www-address to $www"
    echo ""

    read -p "What is your Package-string (de.jedamus-solutions): " package
  fi
else
  email="$1"
  www="$2"
  package="$3"
fi

if [ -f ${CH}.modify_me ]; then
  echo "modifying ${CH}.modify_me to ${CH}.py"
  cat ${CH}.modify_me | sed "s#__EMAIL__#${email}#" | \
                        sed "s#__WWW__#${www}#" | \
		        sed "s#__PACKAGE__#${package}#" > ${CH}.py
  echo "removing ${CH}.modify_me"
  rm -f ${CH}.modify_me
fi
#chmod +x ${CH}.py

# vim:ai sw=2

