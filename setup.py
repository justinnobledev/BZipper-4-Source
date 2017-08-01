#!/usr/bin/python2
from distutils.core import setup
import py2exe
import sys
import os 

if len(sys.argv) == 1:
	sys.argv.append("py2exe")

setup( options = {"py2exe": {"compressed": 1, "optimize": 2,"dll_excludes": "w9xpopen.exe",'dist_dir': "../Bzipper", "ascii": 0, "bundle_files": 1}},
		zipfile = None,

		console = [
		{
			"script": "main.py",                    ### Main Python script
			"dest_base" : "Bzipper"
		}
	],)

os.system('upx -9 dist/*.exe')
os.system("rmdir /s /q build")
os.system("del /q *.pyc")