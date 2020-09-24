from tkinter import *
import pygame
import os

#Define Music Player Class
class MusicPlayer:
	#Define Costructor
	def __init__(self,root):
		self.root=root
		self.root.title("Music Player") #Title of the window
		self.root.geometry("1000x200+200+200")#Window size
		pygame.init()#install pygame
		pygame.mixer.init()
		self.track=StringVar()
		self.status=StringVar()

		#Creating track frame for song label and status label
		trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
		trackframe.place(x=0,y=0,width=600,height=100)

		#Inserting Song track label
		songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)

		#Inserting Status label
		trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)

		#Creating Buttons
		buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
		buttonframe.place(x=0,y=100,width=600,height=100)

		#Inserting Play Buttons
		playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)

		#Inserting Pause Buttons
		playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)

		#Inersting Unpause Buttons
		playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)

		#Inserting Stop Buttons
		playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)

		#Creating Playlist Frame
		songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
		songsframe.place(x=600,y=0,width=400,height=200)

		#Inserting scrollbar
		scrol_y=Scrollbar(songsframe,orient=VERTICAL)

		#Inserting Playlist listbox
		self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)

		#Applying Scrollbar to listbox
		scrol_y.pack(side=RIGHT,fill=Y)
		scrol_y.config(command=self.playlist.yview)
		self.playlist.pack(fill=BOTH)

		#Changing directory for fetching songs
		os.chdir("G:/Music/Guru")

		#Fetching song list
		songtracks=os.listdir()

		#Inserting songs into playlist
		for track in songtracks:
			self.playlist.insert(END,track)

	# Define  play song function
	def playsong(self):
		self.track.set(self.playlist.get(ACTIVE))
		self.status.set("-Playing")
		pygame.mixer.music.load(self.playlist.get(ACTIVE))
		pygame.mixer.music.play()

	#Define stop song
	def stopsong(self):
		self.status.set("-Stopped")
		pygame.mixer.music.stop()

	#Define pause song
	def pausesong(self):
		self.status.set("-Paused")
		pygame.mixer.music.pause()

	#Define unpause song
	def unpausesong(self):
		self.status.set("-Playing")
		pygame.mixer.music.unpause()

root=Tk()
MusicPlayer(root)
root.mainloop()