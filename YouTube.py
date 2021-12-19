from pytube import YouTube
import os
from mhmovie.code import *

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

link = input(color.BOLD+color.GREEN+"Enter YouTube video link: "+color.END)
yt = YouTube(link)

f=yt.length/60
g = float("{:.2f}".format(f))
print(color.UNDERLINE+color.BOLD+color.GREEN+"Information about video :-" +color.END)
print(color.BOLD+color.PURPLE+"Title: "+color.END,yt.title)
print(color.BOLD+color.PURPLE+"Views: "+color.END,yt.views)
print(color.BOLD+color.PURPLE+"Length: "+color.END, g, color.BOLD+"Min"+color.END)
print(color.BOLD+color.PURPLE+"Ratings: "+color.END,yt.rating)
print(color.BOLD+color.PURPLE+"Discription: "+color.END,yt.description)


x=input(color.BOLD+color.CYAN+"Enter the format in which you want to download: \n1.Video \n2.Audio\n"+color.END)


if(x=='1'):
    a=input("Enter Resolution:- \n1.1080p \n2.720p \n3.480p \n4.360p \n5.240p\n")
    v_name=yt.title+".mp4"

    if(a=='1'):
        itag=137
    elif(a=='2'):
        itag=136
    elif(a=='3'):
        itag=135
    elif(a=='4'):
        itag=134
    elif(a=='5'):
        itag= 133
    else: print(color.BOLD+"Invalid Choice / Video Not found in this resolution"+color.END)

    yv = yt.streams.get_by_itag(itag)   
    ya = yt.streams.get_by_itag(140)
    print(color.BOLD+color.PURPLE+"Downloading...."+color.END)
    yv.download('YouTube Downloader',filename="video")
    ya.download('YouTube Downloader',filename="audio")
    
    video = movie("YouTube Downloader/video.mp4")
    audio = music('YouTube Downloader/audio.mp4')
    final = video + audio
    final.save("YouTube Downloader/"+v_name)
    os.remove('YouTube Downloader/video.mp4')
    os.remove('YouTube Downloader/audio.mp4')
    print(color.BOLD+color.PURPLE+"Downloaded."+color.END)

elif(x=='2'):
    itag=140
    a_name=yt.title+" audio"

    ys = yt.streams.get_by_itag(itag)
    print(color.BOLD+color.PURPLE+"Downloading....")
    ys.download('YouTube Downloader/',filename=a_name)
    print("Downloaded."+color.END)

else:print((color.BOLD+color.YELLOW+"INVALID CHOICE "+color.END))