import pytube

url = "https://www.youtube.com/watch?v=000al7ru3ms"
#Load url in youtube funnction
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download('./Downloads')
