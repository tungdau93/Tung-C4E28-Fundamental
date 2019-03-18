from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode("utf-8")
soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section", "section chart-grid")

li_list = section.find_all("li")
song_list = []
for li in li_list:
    h3_names = li.h3
    a_names = h3_names.a
    names = a_names.string
    # print(names)

    h4_artists = li.h4
    a_artists = h4_artists.a
    artists = a_artists.string
    # print(artists)

    song_dict = OrderedDict({
        "Name" : names,
        "Artist" : artists
    })
    song_list.append(song_dict)

pyexcel.save_as(records = song_list, dest_file_name = "Songs.xls")


for each_list in song_list:
    search_songs = each_list["Name"] + " - " + each_list["Artist"]
    # print(search_songs)
    option = {
        "default_search": "ytsearch",
        "max_downloads": 1
    }
    dl = YoutubeDL(option)
    dl.download([search_songs])



