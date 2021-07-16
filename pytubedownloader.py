from pytube import YouTube

def video_download(youtube_link):
    myStream = YouTube(youtube_link).streams.first()
    myStream.download()
    return myStream.title
     