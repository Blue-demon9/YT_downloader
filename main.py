import pytube

path = "~/Downloads"
inp = input("""
do you want to download video by:
1.pasting the video link
2.searching video by name
3.download playlist
4.download from Channel
:""")
if inp == "1":
    url = input("Paste the link here: ")
    yt = pytube.YouTube(url)
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(22)
    print(f"Downloading: \n{yt.title}")
    stream.download(path)
    print("Download is complete!")
elif inp == '2':
    name = input("Enter the video name to search: ")
    sr = pytube.Search(name)
    print(f"There are {len(sr.results)} results for your search.")
    sr.results()
elif inp == '3':
    url = input("Paste the playlist link: ")
    p = pytube.Playlist(url)
    print(f"Downloading: {p.title}")
    for video in p.videos:
        video.streams.first().download()
elif inp == '4':
    chan = input("paste the channel link: ")
    c = pytube.Channel(chan)
    for url in c.video_urls[:10]:
        print(url)
