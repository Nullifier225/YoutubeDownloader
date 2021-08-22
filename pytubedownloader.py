    from pytube import YouTube

    def video_download():
        youtube_link =YouTube('https://youtu.be/U0tOvqAmcb8')
        myStream = youtube_link.streams.filter(only_audio=True)
        myStream.download() 

    if __name__ == '__main__':
        video_download()
        