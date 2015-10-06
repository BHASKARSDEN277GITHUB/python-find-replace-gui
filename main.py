__author__="Bhaskar Kalia"
__date__="Mon Sep 14"
__description__="Find and Replace Tool/gui interface"

#!/usr/bin/env


from Tkinter import *
import tkMessageBox
import subprocess
from Replacer import *


"""
###testing without gui###
filename="/home/bhaskar/Documents/test.txt"
replacer=Replacer(filename,"kalia","bhaskar")
replacer.find_and_replace()
print("done")
subprocess.call("gnome-open "+filename,shell=True)
"""

class Application(Frame):
	#method to start find and replace
	def fire(self):
		filepath=self.filepath.get("1.0","end-1c")
		find_text=self.find_text.get("1.0","end-1c")
		replace_text=self.replace_text.get("1.0","end-1c")
		#create replacer object and call find_and_replace method
		replacer=Replacer(filepath,find_text,replace_text)
		replacer.find_and_replace()
		
		#enable the open output file button
		self.show.config(state="normal")
		print("done")
	
	#method to open output file
	def open_output(self):
		filepath=self.filepath.get("1.0","end-1c")
		subprocess.call("gnome-open "+filepath,shell=True)

	#method to create widgets
	def create_widgets(self):
		#label1  filepath
		self.label1=Label(self,text="Enter Absolute Path of File")
		self.label1.pack()

		#creating a textBox for reading the filepath value
		self.filepath=Text(self)
		self.filepath["height"]=1
		self.filepath["width"]=60
		self.filepath.insert(END,"/home")
		self.filepath.pack(padx=20)

		#label2 find text
                self.label2=Label(self,text="Enter Text to Find") 
                self.label2.pack()

		#creating a textBox for reading the find text
		self.find_text=Text(self)
                self.find_text["height"]=1
                self.find_text["width"]=60
                self.find_text.insert(END,"Text to find")               
                self.find_text.pack(padx=20)

		#label3 replace text
                self.label3=Label(self,text="Enter Text to Replace")         
                self.label3.pack()

                #creating a textBox for reading the find text
                self.replace_text=Text(self)
                self.replace_text["height"]=1
                self.replace_text["width"]=60
                self.replace_text.insert(END,"Text to replace")
                self.replace_text.pack(padx=20)

		#Fire button here
		self.firebutton=Button(self)
		self.firebutton["text"]="Fire"	
		self.firebutton["fg"]="black"
		self.firebutton["command"]=self.fire
		self.firebutton.pack(padx=20,pady=10)
		
		
		#show output files button button here
		self.show=Button(self)
		self.show["fg"]="black"
		self.show["width"]=21
		self.show["text"]="Open Output File"
		self.show["command"]=self.open_output
		self.show.config(state="disabled") #disbaled until sed has not been completed
		self.show.pack()

		#exit button here
		self.exit=Button(self)
		self.exit["fg"]="red"
		self.exit["text"]="Exit"
		self.exit["command"]=self.quit

		self.exit.pack(padx=20,pady=10)

		#created by and all details
		self.ref=Label(self)
		self.ref["bg"]="black"
		self.ref["fg"]="white"
		self.ref["text"]="Created By : Bhaskar Kalia\nSoftware Engineer I\nSnapdeal\n"
		self.ref.pack(side="bottom")
		

	#constructor
	def __init__(self,master=None):
		#set title for windows (find and replace)
		master.title("Find and Replace")
	
		# Define frame size and position in the screen :
		"""
       		ScreenSizeX = master.winfo_screenwidth()  # Get screen width [pixels]
       		ScreenSizeY = master.winfo_screenheight() # Get screen height [pixels]
       		ScreenRatio = 0.5                              # Set the screen ratio for width and height
       		
		FrameSizeX  = int(ScreenSizeX * ScreenRatio)
		
       		FrameSizeY  = int(ScreenSizeY * ScreenRatio)
        	FramePosX   = (ScreenSizeX - FrameSizeX)/2 # Find left and up border of window
      		FramePosY   = (ScreenSizeY - FrameSizeY)/2
		
		#position frame in the center
      		master.geometry("%sx%s+%s+%s"%(FrameSizeX,300,50,200))
		"""

		Frame.__init__(self,master)
		self.pack(padx=20, pady=20)
		self.create_widgets()
		
		


#start gui
root=Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
