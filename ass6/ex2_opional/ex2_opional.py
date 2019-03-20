from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
data = conn.read()
html_content = data.decode("utf-8")
soup = BeautifulSoup(html_content, "html.parser")

table_title = soup.find("table", id = "tblGridData")
td_list = table_title.find_all("td", "h_t")
col_list = []
for td in td_list:
    col_list.append(td.string)

table_content = soup.find("table", id = "tableContent")
rows_list = table_content.find_all("tr")
excel_table = []









