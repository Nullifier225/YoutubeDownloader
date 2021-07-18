from pytube import YouTube

def video_download(youtube_link):
    myStream = YouTube(youtube_link).streams.filter(only_audio=True)
    return myStream
     