import requests
from bs4 import BeautifulSoup
from Tkinter import *
import sys
import os
import time

def mhello():
	MyMain()



def MyMain():
	
	root =Tk()
	root.geometry('650x650+600+500')
	root.title('Amazon Webscraper')
	Mbutton = Button(root,text='Restart',command =mhello).pack()
	#slider = Scale(root,orient=VERTICAL,length=300,width=20,sliderlength=20,from_=0,to=50,tickinterval=2)
	#slider.pack()
	scrollbar = Scrollbar(root)
	scrollbar.pack(side=RIGHT,fill = Y)
	mylist = Listbox(root,yscrollcommand=scrollbar.set,height = 400,width=500)
	
	mylist.pack(side=LEFT,fill = BOTH)
	scrollbar.config(command = mylist.yview)
	#for line in range(100):

	print("Begining Process")
	f= open('asin.text','r')
	f2=open('userAgents','r')
	Agents=f2.readlines()
	lines =f.readlines()
	x =1
	headers = 'user-agent'
	#for line in range(100):
		#mylist.insert(END,'New Product')

	for line in lines:
		#if x > 3:
		#	headers ={'user-agent' : Agents}

#			x = 0

		t0 = time.time()
		string2='https://www.amazon.com/gp/offer-listing/'
		string3='/ref=dp_olp_new_mbc?ie=UTF8&mv_size_name=all'
		string4=string2+"".join([str(i) for i in line])+string3
		r = requests.get(string4)
		r.content
		soup = BeautifulSoup(r.content)
		print x
		proName = soup.find_all("title",{"dir":"ltr"})
		for item in proName:
			print item.text
			var = item.text
			#theLabel = Label(root,text=var)
			#heLabel.pack()
			mylist.insert(END,"###########################################################################")
			mylist.insert(END,"Item number:",x)
			mylist.insert(END,var,"\n")
			mylist.insert(END,line,"\n\n")
			time.sleep(1)

		g_data = soup.find_all("span",{"class":"a-offscreen"})
		print ("New Product")
		for item in g_data:
			test = item.text
			print test
			var = item.text
			#theLabel = Label(root,text=var)
			#theLabel.pack()
			mylist.insert(END,var,)
			time.sleep(1)
		mylist.insert(END,'\n\n')	
		x = x+1
		line =f.readline()
		#response_delay = time.time()-t0
		time.sleep(1)	
	print ("Process Finished")
	f.close
	f2.close
	root.mainloop()

MyMain()