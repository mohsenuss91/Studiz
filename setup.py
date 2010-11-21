from distutils.core import setup
import py2exe

import os
# --packages encodings.latin_1

Mydata_files = []
for files in os.listdir('images/'):
	f1 = 'images/' + files
	if os.path.isfile(f1): # skip directories
		f2 = 'images', [f1]
        Mydata_files.append(f2)


Mydata_files.append(('styles', ['styles/style.css']))
setup(name = 'Studiz',
			version = '1.0',
			author ='Redouane',
			author_email="unrealdz@gmail.com", 
			data_files = Mydata_files,
			windows=[ { 
							"script": 'Studz.py',
							"icon_resources": [(1, "images/app.ico") ]

					} ],
	
			options={"py2exe": {"includes": ["sip"]}}) 
			
			
