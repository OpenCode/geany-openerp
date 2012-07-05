This repository is a collection of configuration files to help developers of **OpenERP** modules that use the editor **Geany** for their work.

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
* super = super for function inherith
* raise = raise error message
* pdb = debugger import
* python\_py = \_\_openerp\_\_.py file structure
* create = create ORM method
* write = write ORM method
* unlink = unlink ORM method
* browse = browse ORM method
* search = search ORM method

**XML CODE**

* tree = new tree structure
* tree_in = inherited tree structure
* form = new form structure
* form_in = inherited form structure
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

Questo repository è una raccolta di file di configurazione utili agli sviluppatori di moduli di **OpenERP** che utilizzano l'editor **Geany** per il loro lavoro.

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
* pdb = import del debugger
* python\_py = struttura del file \_\_openerp\_\_.py
* create = metodo dell'ORM create
* write = metodo dell'ORM write
* unlink = metodo dell'ORM unlink
* browse = metodo dell'ORM browse
* search = metodo dell'ORM search

**CODICE XML**

* tree = struttura nuova tree
* tree_in = struttura tree ereditata
* form = struttura nuovo form
* form_in = struttura form ereditata
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
