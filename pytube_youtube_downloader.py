from pytube import YouTube                              # pip install pytuube


# Defined - 01
url = 0                                                 # define null url
selected_resolution = '720p'                            # Resolution


# Single Link Downloader
def single_link(url):
    # resultion_chooser()
    video = YouTube(url)                                # Video defined for operation
    print('\n\n\nDonwloading... .. ..', video.title)
    YouTube(
            url,
            allow_oauth_cache=True
        ).streams.filter(res=selected_resolution,file_extension='mp4').get_highest_resolution().download('./Downloads')

    # Finished
    print('Downloaded, Check your Downloads folder in this root folder.')


# Playlist Downloader
def playlist_link(url):
    print('Playlist downloader will be coming soon...')




#
#   ----- Start from here
#
print('==================== The Youtube Downloader\n')
single_or_playlist = input('Enter your yutube link if this is single video or your video link is playlist Enter "no"? Enter Link or URL/no : ')


if single_or_playlist == 'yes':
    print('\n\n================= Single video link or URL')
    url = single_or_playlist
    single_link(url)

elif single_or_playlist == 'no':
    print('\n\n================= Playlist Videos URL: ')
    url = input('Enter/Paste Youtbe Link or URL : ')
    playlist_link(url)

else:
    print('\n\n================= Single video link or URL')
    url = single_or_playlist
    single_link(url)




# def resultion_chooser():
#     print('==================== Video Resolution\n')
#     print('Enter 1 for 1080p .mp4 formate video')
#     print('Enter 2 for 720p .mp4 formate video')
#     print('Enter 3 for 480p .mp4 formate video')
#     # single_or_playlist = input('Enter any number : ')


