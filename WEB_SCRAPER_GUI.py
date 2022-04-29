import requests
import html5lib
import bs4
import sys
import time
import threading
from tkinter import *

###################################

win = Tk()
win.title("Scrape any Website")

def scrappin():

	url = requests.get(URL.get())
	res = bs4.BeautifulSoup(url.text , "html.parser")
	timestr = time.strftime("_%Y_%m_%d_%H_%M_%S")


	#######webcode only file
	try:
		saveFile2 = open("WEB_CODE"+timestr+".txt","a")
	
		for i in res.select(pvar.get()):
			try:
				saveFile2.write(i.prettify())
			
			except:
				error1 = open("LOG"+timestr+".txt","a")
				error1.write("error1\n")
				#print('error1')

	except:
		e1 = open("LOG"+timestr+".txt","a")
		e1.write("e1\n")
		#print('e1')
	
	finally:
		saveFile2.close()

	######file to save web text
	try:
		saveFile1 = open("WEB_TEXT"+timestr+".txt","a")
	
		for i in res.select(pvar.get()):
			try:
				saveFile1.write(i.getText())
				saveFile1.write("\n\t")
			except:
				error2 = open("LOG"+timestr+".txt","a")
				error2.write("error2\n")
				#print("error2")

	except:
		e2 = open("LOG"+timestr+".txt","a")
		e2.write("e2\n")
		#print("e2")
	
	finally:
		saveFile1.close()	

	#will execute def scrappin periodically
	if perio.get() > 0:
		threading.Timer(perio.get(),scrappin).start()
	

################################

#var variable is a String variable
var = StringVar()

#contains the text of label
var.set("Website Scrapper Tool")

#Label within the window....
LABEL_OF_WEB=Label(win,textvariable=var,bd=10,bg="cyan",font=("Calibre",38)).grid(row=0,column=0)

#StringVar to pass the url to the function
URL = StringVar()
pvar = StringVar()
perio = IntVar()

#entry box
url_label = Label(win,text="URL= ",font=7).place(x=2,y=93)
E1=Entry(win,bd=5,font=7,textvariable=URL,width=50).grid(row=1,column=0,padx=0,pady=12)

tags_label = Label(win,text="tags/class/ids= ",font=7).place(x=30,y=131)
E2=Entry(win,bd=5,font=7,textvariable=pvar,width=10).place(x=145,y=130)

time_label = Label(win,text="Seconds=",font=7).place(x=300,y=133)
E3=Entry(win,bd=5,font=7,textvariable=perio,width=4).place(x=380,y=130)

#Button
button=Button(win,text="Scrape it",bd=5,command=scrappin).grid(row=2,column=0,pady=50)

############################################
win.mainloop()