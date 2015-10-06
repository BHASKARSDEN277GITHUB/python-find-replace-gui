__author__="Bhaskar Kalia"              
__date__="Mon Sep 14"                   
__description__="Find and Replace Tool/Replacer class" 

#!/usr/bin/env

import subprocess

class Replacer:
	def __init__(self,filename,f_text,r_text):
		self.filename=filename
		self.f_text=f_text
		self.r_text=r_text
	
	def find_and_replace(self): #find and replace text
		command="sed -i 's/"+self.f_text+"/"+self.r_text+"/g' "+self.filename
		print(command)
		subprocess.call(command,shell=True) 

	def open_file(self): #open the new file with gnome-open filename
		command="gnome-open "+self.filename
		subprocess.call(command,shell=True)

	
	
