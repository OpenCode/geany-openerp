This repository is a collection of configuration files to help developers of **OpenERP** modules that use the editor **Geany** for their work.
To install the files is possible to follow the instruction:

## templates

Contains the filetype to create rapidly new standard openerp file

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

## tags

Contains the OpenERP ORM functions declaration to show the correct use of a function while write it

*INSTALLATION*

Copy (or link) all the files in "tags" folder in ~/.config/geany/tags

*USE*

Write an OpenERP ORM function to see the correct declaration in a tooltip

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
* m2m = field many2many
* related = field related
* fnct = field function
* def_fnct = function definition related to function field
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
* copy = copy ORM method
* copy_data = copy_data ORM method

**XML CODE**

* field = field tag
* tree = new tree structure
* tree_in = inherited tree structure
* form = new form structure
* form7 = new form structure with OpenERP 7 specific tag
* form_in = inherited form structure
* xpath = xpath structure
* kanban = kanban structure
* menu = menu structure
* search = search structure
* search_in = inherited search structure
* action = action structure
* button = object button
* button_action = action button
* notebook = notebook structure
* filter = filter field in search view
* group_by = filter field with group by context
* context = context field
* domain = domain field
* help = help tag used in the action structure
* attrs = complete attrs field tag


Questo repository è una raccolta di file di configurazione utili agli sviluppatori di moduli di **OpenERP** che utilizzano l'editor **Geany** per il loro lavoro.
Per l'installazione è possibile seguire le istruzioni riportate di seguito:

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

## tags

Contiene le dichiarazioni delle funzioni dell'ORM di OpenERP per mostrare il loro uso corretto mentre le si scrive

*INSTALLAZIONE*

Copiare (o linkare) tutti i file della cartella "tags" in ~/.config/geany/tags

*USO*

Scrivere una funzione dell'ORM di OpenERP per mostrare il tooltip con la corretta dichiarazione

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
* m2m = field many2many
* related = field related
* fnct = field function
* def_fnct = definizione della funzione lagata ad un campo function
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
* copy = metodo dell'ORM copy
* copy_data = metodo dell'ORM copy_data

**CODICE XML**

* field = tag field
* tree = struttura nuova tree
* tree_in = struttura tree ereditata
* form = struttura nuovo form
* form7 = struttura nuovo form con tag specifici di OpenERP 7
* form_in = struttura form ereditata
* xpath = struttura xpath
* kanban = struttura kanban
* menu = struttura menu
* search = struttura search
* search_in = struttura search ereditata
* action = struttura action
* button = button di tipo object
* button_action = button di tipo action
* notebook = struttura del notebook
* filter = campo filter nella vista search
* group_by = campo filter con context di raggruppamento già popolato
* context = campo context
* domain = campo domain
* help = campo help da usare nelle action
* attrs = tag attrs dei campi completo

