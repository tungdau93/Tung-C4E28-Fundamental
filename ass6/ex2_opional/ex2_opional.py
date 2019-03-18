from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

raw_data = conn.read()
html_content = raw_data.decode("utf-8")
with open("scafe.html", "wb") as f:
    f.write(raw_data)

soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())
table = soup.find("table", id = "tblGridData")
# print(table.prettify())
td_list = table.find_all("td")
# print(td_list)
rows_list = []
for td in td_list:
    rows = td.string
    rows_list.append(rows)
pyexcel.save_as(records = rows_list, dest_file_name = "scafe.xls")



















