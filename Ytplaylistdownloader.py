from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
#from PIL import Image, ImageTk
from pytube import Playlist
import time
import threading
import os

def select_path():
    #allows user to select path
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_filemp4():
    #downloads mp4
    get_link = link_field.get()
    user_path = path_label.cget("text")
    mp4 = Playlist(get_link)
    tasks = len(mp4.video_urls)
    x = 0
    speed = 1
    while(x<tasks):
        for video in mp4.videos:
            video.streams.get_highest_resolution().download(user_path)
            time.sleep(0.01)
            bar['value']+=(speed/tasks)*100
            x+=speed
            percent.set(str(int((x/tasks)*100))+"%")
            text1.set(str(x)+"/"+str(tasks)+" download completed")
            screen.update_idletasks()

def mp4_download_start():
    threading.Thread(target=download_filemp4).start()

def download_filemp3():
    #downloads mp3
    get_link = link_field.get()
    user_path = path_label.cget("text")
    mp3 = Playlist(get_link)
    tasks = len(mp3.video_urls)
    x = 0
    speed = 1
    while(x<tasks):
        for video in mp3.videos:
            audioStream = video.streams.get_by_itag(140)
            out_file = audioStream.download(output_path=user_path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            time.sleep(0.01)
            bar['value']+=(speed/tasks)*100
            x+=speed
            percent.set(str(int((x/tasks)*100))+"%")
            text1.set(str(x)+"/"+str(tasks)+" download completed")
            screen.update_idletasks()

def mp3_download_start():
    threading.Thread(target=download_filemp3).start()

screen = Tk()
title = screen.title('Youtube Playlist MP3/MP4 Downloader')
img = PhotoImage(file='appicon.ico')
screen.iconphoto(False, img)
canvas = Canvas(screen, width=600, height=400)
canvas.pack()

#refresh window
def refresh_field():
    link_field.config(textvariable=link)
    link.set(str(""))
    bar["value"]=0
    percent.set(str(""))
    text1.set(str(""))

#image background
#img = Image.open('YouTubePlaylistToMP3/wampiss.png')
#resize and display
#img = img.resize((600, 400))
#img = ImageTk.PhotoImage(img)
#canvas.create_image(300, 200, image=img)

#Header
header1 = Label(screen, text="YouTube Playlist Downloader", font=('Arial, 20'))
header2 = Label(screen, text="by:TroyUrtiz", font=('Arial, 6'))

#defining percent and text labels
link = StringVar()
percent = StringVar()
text1 = StringVar()

#Playlist link field
link_label = Label(screen, text="Enter Playlist Download Link: ", font=('Arial, 8'))
link_field = Entry(screen, width=50)
refresh_icon = PhotoImage(file="refresh.png")
refresh_input = Button(screen, image=refresh_icon, command=refresh_field)

#Select Path
path_label = Label(screen, text="Select Path To Save Download", font=('Arial, 8'))
select_btn = Button(screen, text="Browse", command=select_path)

#Progress Bar
bar = Progressbar(screen, orient=HORIZONTAL, length=500, mode='determinate')
percent_label = Label(screen, textvariable=percent)
text_label = Label(screen, textvariable=text1)

#Download Button
btn1 = Button(screen, text="MP4", command=mp4_download_start)
btn2 = Button(screen, text="MP3", command=mp3_download_start)

#Add Widgets to Window
canvas.create_window(300, 50, window=header1)
canvas.create_window(300, 75, window=header2)
canvas.create_window(120, 100, window=link_label)
canvas.create_window(230, 120, window=link_field)
canvas.create_window(60, 120, window=refresh_input)
canvas.create_window(300, 180, window=path_label)
canvas.create_window(84, 180, window=select_btn)
canvas.create_window(300, 220, window=bar)
canvas.create_window(300, 245, window=percent_label)
canvas.create_window(300, 265, window=text_label)
canvas.create_window(510, 120, window=btn1)
canvas.create_window(430, 120, window=btn2)

screen.mainloop()