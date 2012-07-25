#!/usr/bin/python


import os


def insert_data(file, string, replace):

	s = open(file).read()
	s = s.replace(string, replace)
	f = open(file, 'w')
	f.write(s)
	f.close()


def create_structure():

	p = os.popen("zenity --entry --title='Project name'")
	project_name = p.readline()
	p.close()

	p = os.popen("zenity --file-selection --directory --title='Project path'")
	project_path = p.readline()
	p.close()

	if not project_name and not project_path:
		return False

	project_name = project_name.replace("\n", "").lower()
	project_path = project_path.replace("\n", "")
	
	complete_path = '%s/%s' % (project_path, project_name)

	print project_name, project_path, complete_path
	
	os.makedirs('%s/' % complete_path)
	os.makedirs('%s/%s/' % (complete_path, project_name))
	os.makedirs('%s/l18n/' % complete_path)
	os.system('cp ~/.config/geany/templates/files/__openerp__.py %s/' % (complete_path))
	insert_data('%s/__openerp__.py' % (complete_path), "'name': \"\"", "'name': \"%s\"" % (project_name))
	os.system('cp ~/.config/geany/templates/files/__init__.py %s/' % (complete_path))
	insert_data('%s/__init__.py' % (complete_path), "import", "import %s" % (project_name))
	os.system('cp ~/.config/geany/templates/files/__init__.py %s/%s/' % (complete_path, project_name))
	insert_data('%s/%s/__init__.py' % (complete_path, project_name), "import", "import %s" % (project_name))
	
	os.system("zenity --info --text \"OpenERP Module Structure Created in: %s!\"" % complete_path)

create_structure()

