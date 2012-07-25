#!/usr/bin/bash

echo 'Geany OpenERP Utility'
echo 'Francesco OpenCode Apruzzese <info@e.ware.org>'
echo 'Installing geany_openerp files'

echo 'Remove old files'
if [ -f ~/.config/geany/geany.conf ]; then
    rm ~/.config/geany/geany.conf
fi

if [ -f ~/.config/geany/snippets.conf ]; then
    rm ~/.config/geany/snippets.conf
fi

if [ -d ~/.config/geany/templates/ ]; then
    rm -r ~/.config/geany/templates/
fi

if [ -d ~/.config/geany/scripts/ ]; then
    rm -r ~/.config/geany/scripts/
fi


echo 'Install configuration file'
cp -f geany.conf ~/.config/geany/
echo 'Install snippets file'
cp -f snippets.conf ~/.config/geany/

echo 'Install template files'
cp -R -f templates/ ~/.config/geany/
echo 'Install scripts'
cp -R -f scripts/ ~/.config/geany/


echo 'All the geany files are now installed!'
echo 'Thank you for your choice!'
