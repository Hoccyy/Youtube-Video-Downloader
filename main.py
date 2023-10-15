def imageDownload(imageUrl:str, imageName: str):
    import requests
    # Download Data from URL
    response = requests.get(imageUrl)
    open(imageName, 'wb').write(response.content)


def downloadVideo(video_url: str, path: str):
    from pytube import YouTube
    
    try:
        youtubeInstance =  YouTube(video_url)
        video = youtubeInstance.streams.get_highest_resolution()
        video.download(path)
        return 1
    except:
        return 0

def playListUrlFetch(playlistUrl: str):
    from pytube import Playlist

    playlist = Playlist(playlistUrl)
    print('Number of videos in playlist: %s\n' % len(playlist.video_urls))

    return playlist.video_urls


#
operationType = input('One video(S) or playlist(P) : ')

if operationType in ['S', 's']:
    downloadVideo(
        input('Enter Video URL : '), 
        input('Enter download path/blank for current dir : ')
    )

if operationType in ['P', 'p']:
    videosDownloaded = 0
    directoryChoice = input('Enter directory for videos(recommended) : ')

    for videoURL in playListUrlFetch(input('Enter playlist URL : ')):
        videosDownloaded +=(
            downloadVideo(
                videoURL, 
                directoryChoice
            ))
    print ('%d Videos downloaded' % videosDownloaded)