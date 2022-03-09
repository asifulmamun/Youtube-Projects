from pytube import YouTube              # pip install pytuube


# Defined - 01
url = 0



print('==================== The Youtube Downloader\n')
single_or_playlist = input('Do you want to download single youtube video? Enter yes/no : ')


if single_or_playlist == 'yes':
    print('\n\n================= Single video link or URL')
    url = input('Enter/Paste Youtbe Link or URL : ')
    single_link(url)

elif single_or_playlist == 'no':
    print('\n\n================= Playlist Videos URL: ')
    url = input('Enter/Paste Youtbe Link or URL : ')
    playlist_link()

else:
    print('\n\n================= Single video link or URL')
    url = input('Enter/Paste Youtbe Link or URL : ')
    single_link(url)


# Define - 02
video = YouTube(url)                    # Video defined for operation 
selected_resolution = '720p'            # Resolution


print('==================== Video Resolution\n')
print('Enter 1 for 1080p .mp4 formate video')
print('Enter 2 for 720p .mp4 formate video')
print('Enter 3 for 480p .mp4 formate video')
single_or_playlist = input('Enter any number : ')


# Single Link Downloader
def single_link(url):
    print(video.title)                                  # Titile
    print('Donwloading... ... ... ...')                 # Continue sign
    YouTube(
            url,
            allow_oauth_cache=True
        ).streams.filter(res=selected_resolution,file_extension='mp4').get_highest_resolution().download('./Downloads')

    # Finished
    print('Downloaded, Check your Downloads folder in this root folder.')


# Playlist Downloader
def playlist_link(url):
    print('Playlist downloader will be coming soon...')