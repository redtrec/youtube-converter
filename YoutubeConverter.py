from pytube import YouTube
formatCheck = False
while formatCheck == False:
    print("========== YOUTUBE TO MP3 / MP4 CONVERTER ==========")
    yt = YouTube(input("Enter the link: "))
    print(yt.title)
    print(yt.thumbnail_url)
    print("[1] MP3")
    print("[2] MP4")
    format = input("Enter the format you desire: ")
    if format == "1":
        formatCheck = True
        audioStreams = yt.streams.filter(only_audio=True)
        for x in audioStreams:
            print(x)
        streamNumber = input("Enter the itag of your chosen stream: ")
        stream = yt.streams.get_by_itag(streamNumber)
        stream.download()
    elif format == "2":
        formatCheck = True
        video = (yt.streams.filter(file_extension='mp4'))
        progressiveVideoStreams = yt.streams.filter(progressive=True) # Progressive - audio and video in a single file
        for x in progressiveVideoStreams:
            print(x) 
        videoNumber = input("Enter the itag of your chosen stream: ")
        stream = yt.streams.get_by_itag(videoNumber)
        stream.download()
    else:
        print("Wrong input")
        continue
