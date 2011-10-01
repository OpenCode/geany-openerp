This repository is a collection of configuration files to help developers of **OpenERP** modules that use the editor **Geany** for their work.

### snippets.conf

Contains the definition of different snippets of code used within the files .py

*INSTALLATION*

Copy snippets.conf file in ~/.config/geany

*USE*

Just type keywords below and press TAB button to get the auto-insertion of the snippet

  oclass = class structure
  ocol = _column structure	
  ochar = fields.char('', size = 64),
  ointeg = fields.integer(''),
  obool = fields.boolean(''), 
  ofloat = fields.float(''),
  otext = fields.text(''),
  odate = fields.date(''),
  odatetime = fields.datetime(''),
  oselec = field.selection(
		(('', ''),('','')),
		'')

Questo repository è una raccolta di file di configurazione utili agli sviluppatori di moduli di **OpenERP** che utilizzano l'editor **Geany** per il loro lavoro.

#### snippets.conf

Contiene la definizione di diversi snippet di codice da usare all'interno dei file .py

*INSTALLAZIONE*

Copiare il file snippets.conf in ~/.config/geany

*USO*

Basta digitare una delle parole chiave che seguono e digitare TAB per ottenere l'autoinserimento dello snippet

  oclass = struttura di una classe
  ocol = struttura delle colonne
  ochar = fields.char('', size = 64),
  ointeg = fields.integer(''),
  obool = fields.boolean(''), 
  ofloat = fields.float(''),
  otext = fields.text(''),
  odate = fields.date(''),
  odatetime = fields.datetime(''),
  oocselec = field.selection(
		(('', ''),('','')),
		'')
