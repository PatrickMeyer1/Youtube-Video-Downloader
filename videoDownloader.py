# import Tkinter libraries
import tkinter as tk

# import youtube library
from pytube import YouTube

# Uses Youtube to find and download linked video
def download_video():

    try:

        videoUrl = YouTube(link.get())
        video = videoUrl.streams.get_by_itag(22)
        video.download()
        tk.Label(root,text="Video was successfully downloaded", font=("Helvetica", 15)).place(relx=0.5,rely=0.5,anchor="center")
    except:
        tk.Label(root,text="Video was not able to be downloaded", font=("Helvetica", 15)).place(relx=0.5,rely=0.5,anchor="center")

root = tk.Tk()
root.geometry("400x400")
root.title("Youtube Video Downloader")

# Locks the resizing feature
root.resizable(0,0)

tk.Label(root,text="Download Videos here!", font=("Helvetica", 24)).pack()
tk.Label(root,text="Video Link: ", font=("Helvetica", 20)).pack()

link = tk.Entry(textvariable=str)
link.pack()
tk.Button(root,text="Begin Download", font=("Helvetica", 16),background='grey',padx=3,pady=3,command=download_video).place(relx=0.5,rely=0.35,anchor="center")

root.mainloop()



