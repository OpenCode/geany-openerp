This repository is a collection of configuration files to help developers of **OpenERP** modules that use the editor **Geany** for their work.
To install the files is possible to launch the install.sh script in a terminal or follow the instruction:

## templates

Contains the filetype to create rapidly new basci standard openerp file

*INSTALLATION*

Copy (or link) all the files in "templates/files" folder in ~/.config/geany/template/files

Go to Modify -> Preference -> Models and set the parameters

*USE*

Go to File -> New from template

and select your base file from:

* \_\_openerp\_\_.py
* openerp_class.py
* openerp_view.xml
* wizard.py
* wizard_view.xml

## snippets.conf

Contains the definition of different snippets of code used within the files .py

*INSTALLATION*

Copy (or link) snippets.conf file in ~/.config/geany

*USE*

Just type keywords below and press TAB button to get the auto-insertion of the snippet

**PYTHON CODE**

* class = class structure
* cols = _column structure
* defs = _defaults structure
* char = field char
* integ = field integer
* bool = field boolean
* float = field float
* text = field text
* date = field date
* datetime = field datetime
* selec = field selection
* o2m = field one2many
* m2o = field many2one
* fnct = field function
* def_fnct = function definition
* super = super for function inherit
* raise = raise error message
* raise7 = raise error message for OpenERP 7
* pdb = debugger import
* python\_py = \_\_openerp\_\_.py file structure
* create = create ORM method
* write = write ORM method
* unlink = unlink ORM method
* browse = browse ORM method
* search = search ORM method

**XML CODE**

* field = field tag
* tree = new tree structure
* tree_in = inherited tree structure
* form = new form structure
* form7 = new form structure with OpenERP 7 specific tag
* form_in = inherited form structure
* kanban = kanban structure
* menu = menu structure
* search = search structure
* search_in = inherited search structure
* action = action structure
* button = object button
* button_action = action button
* notebook = notebook structure
* filter = filter field in search view
* context = context field
* domain = domain field
* help = help tag used in the action structure
* attrs = complete attrs field tag

##Generate OpenERP Module Structure

It'a a menu that create in 2 steps a OpenERP module structure

*INSTALLATION*

Copy (or link) the folder scripts and file geany.conf in ~/.config/geany

*USE*

Open menu Generate -> Generate OpenERP Module Structure and follow the steps.

Questo repository è una raccolta di file di configurazione utili agli sviluppatori di moduli di **OpenERP** che utilizzano l'editor **Geany** per il loro lavoro.
Per l'installazione è possibile lanciare lo script install.sh in un terminale o seguire le istruzioni riportate di seguito:

## templates

Contiene dei file di base per creare rapidamente dei file standard per openerp

*INSTALLAZIONE*

Copiare (o linkare) tutti i file della cartella "templates/files" in ~/.config/geany/template/files

Cliccare su Modifica -> Preferenze -> Modelli e settare i vari parametri

*USO*

Cliccare su File -> Nuovo da modello

e selezionare il proprio file base tra i seguenti:

* \_\_openerp\_\_.py
* openerp_class.py
* openerp_view.xml
* wizard.py
* wizard_view.xml

## snippets.conf

Contiene la definizione di diversi snippet di codice da usare all'interno dei file .py

*INSTALLAZIONE*

Copiare (o linkare) il file snippets.conf in ~/.config/geany

*USO*

Basta digitare una delle parole chiave che seguono e digitare TAB per ottenere l'autoinserimento automatico dello snippet

**CODICE PYTHON**

* class = struttura di una classe
* cols = struttura _column
* defs = struttura _defaults
* char = field char
* integ = field integer
* bool = field boolean
* float = field float
* text = field text
* date = field date
* datetime = field datetime
* selec = field selection
* o2m = field one2many
* m2o = field many2one
* fnct = field function
* def_fnct = definizione della funzione
* super = ereditare una funzione
* raise = messaggio di errore di raise
* raise7 = messaggio di errore di raise per OpenERP 7
* pdb = import del debugger
* python\_py = struttura del file \_\_openerp\_\_.py
* create = metodo dell'ORM create
* write = metodo dell'ORM write
* unlink = metodo dell'ORM unlink
* browse = metodo dell'ORM browse
* search = metodo dell'ORM search

**CODICE XML**

* field = tag field
* tree = struttura nuova tree
* tree_in = struttura tree ereditata
* form = struttura nuovo form
* form7 = struttura nuovo form con tag specifici di OpenERP 7
* form_in = struttura form ereditata
* kanban = struttura kanban
* menu = struttura menu
* search = struttura search
* search_in = struttura search ereditata
* action = struttura action
* button = button di tipo object
* button_action = button di tipo action
* notebook = struttura del notebook
* filter = campo filter nella vista search
* context = campo context
* domain = campo domain
* help = campo help da usare nelle action
* attrs = tag attrs dei campi completo

##Genera Struttura Modulo OpenERP

È una voce di menu che permette di creare in 2 steps la struttura di un classico modulo OpenERP

*INSTALLAZIONE*

Copiare (o linkare) la cartella scripts ed il file geany.conf in ~/.config/geany

*USO*

Aprire il menu Genera -> Genera Struttura Modulo OpenERP e seguire i vari passi.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/OpenCode/geany-openerp/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

