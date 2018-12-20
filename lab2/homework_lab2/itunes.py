from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL
#1download trang 
url = "https://www.apple.com/itunes/charts/songs"
#1.1 mo ket noi server
conn = urlopen(url)
#1.2 doc data 
raw_data = conn.read()
#1.3 giai ma data
page_content = raw_data.decode("utf8")
#2 vung can quan tam
soup = BeautifulSoup(page_content,"html.parser")
section = soup.find("section","section chart-grid")
div = section.find("div","section-content")
ul = div.find("ul")
#3extract data
li_list = ul.find_all("li")

new_list = []
for li in li_list:
   a3 = li.h3.a
   namesong = a3.string
   a4 = li.h4.a
   artists = a4.string
   news = OrderedDict({
        "NAMESONG": namesong,
        "ARTISTS": artists
    })
   new_list.append(news)
# print(new_list)
#save data to excel
pyexcel.save_as(records = new_list, dest_file_name = "itunes.xlsx")

dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=0I647GU3Jsc&fbclid=IwAR1CTPt6sOT80flPVtdFqUZRZfb3iA4mNpAxBh5QWoOY7MTB2KbSQ3e_It4"])
options = {
    "format":"bestaudio/audio"    
}
dl = YoutubeDL(options)
dl.download(["https://www.youtube.com/watch?v=0I647GU3Jsc&fbclid=IwAR1CTPt6sOT80flPVtdFqUZRZfb3iA4mNpAxBh5QWoOY7MTB2KbSQ3e_It4"])