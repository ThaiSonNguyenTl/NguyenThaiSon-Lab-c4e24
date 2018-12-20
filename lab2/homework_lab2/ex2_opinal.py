from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
#1 download trang
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/2/0/0/bao-cao-tai-chinh-cong-ty-co-phan-sua-viet-nam.chn"
#1.1 mo ket noi server
conn = urlopen(url)
#1.2 doc data
raw_data = conn.read()
#1.3 giai ma data
page_content = raw_data.decode("utf8")
#2 vung roi
soup = BeautifulSoup(page_content,"html.parser")
div = soup.find("div","cf_ResearchDataHistoryInfo")
div1 = div.find("div",id ="divTableHeader")
table = div.find("table",id ="tableContent")
#3extract data
tr_list = table.find_all("tr")
new_list = []
for tr in tr_list:
    td_list = tr.find_all("td","b_r_c")
    for td in td_list:
        td = td.string
        news = {
            "TABLE": td, 
        }
        new_list.append(news)
pyexcel.save_as(records = new_list,dest_file_name = "opinal.xlsx")
