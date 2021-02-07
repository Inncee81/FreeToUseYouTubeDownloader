from pytube import YouTube

url = "https://www.youtube.com/watch?v=000al7ru3ms"

yt = YouTube(url)
print(yt.title)
versions = yt.streams.filter(progressive=True)
for version in versions:
    print(version.resolution)


#video.download('./Downloads')
