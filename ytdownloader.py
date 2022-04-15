from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=C0DPdy98e4c')
yt.title
yt.streams.filter(file_extension='mp4')
stream = yt.streams.get_by_itag(22)
