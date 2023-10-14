def imageDownload(imageUrl:str, imageName: str):
    import requests
    # Download Data from URL
    response = requests.get(imageUrl)
    open(imageName, 'wb').write(response.content)


def downloadVideo(video_url: str, path: str):
    from pytube import YouTube
    youtubeInstance =  YouTube(video_url)
    video = youtubeInstance.streams.get_highest_resolution()
    video.download(path)


downloadVideo(
    input('Enter Video URL : '), 
    input('Enter download path/blank for current dir : ')
)