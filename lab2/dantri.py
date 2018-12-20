from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict #ko bi thay doi thu tu 
#1 download trang
url = "https://dantri.com.vn"
#1.1 mo ket noi server 
conn = urlopen(url)
#1.2 doc data
raw_data = conn.read()
#1.3 decode data
page_content = raw_data.decode("utf8")
# print(page_content)
# # mo file
# f = open("dantri.html","wb") #b de mo raw_data
# f.write(raw_data)
# # dong 
# f.close()
#2 extract ROI(vung quan tam)
soup = BeautifulSoup(page_content, "html.parser")
# print(soup.prettify())
ul = soup.find("ul","ul1 ulnew") #cai "ul" dau la ten the 
# print(ul.prettify())
#3 extract data
li_list = ul.find_all("li")

new_list = []
for li in li_list:
    h4 = li.h4
    a = h4.a
    # a= li.h4.a lam tat
    title = a.string
    link = url+ a["href"]
    news = OrderedDict({
        "title":title,
        "link": link
    })
    new_list.append(news)
    
print(new_list)
#4 save data to exel
pyexcel.save_as(records=new_list, dest_file_name="dan_tri.xlsx")
