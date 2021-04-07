import requests
from bs4 import BeautifulSoup
import lxml
import ast

#url = "https://www.amazon.in/Tecno-Spark-Seabed-Blue-Storage/dp/B087K78FD5/ref=br_msw_pdt-6/261-4433502-0080363?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=D47BXYNXRWJWW97V5E71&pf_rd_t=36701&pf_rd_p=5c669f94-aee5-4b22-81f8-1d301ca2c6a3&pf_rd_i=desktop"
url = "https://www.amazon.in/HP-Laptop-15-6-inch-Screen-Windows/dp/B08XY3843B?ref_=Oct_DLandingS_D_c595c0c7_62&smid=A14CZOWI0VEHLG"


headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
	"Accept-Language" : "en",

}

r = requests.get(url, headers = headers)


soup = BeautifulSoup(r.text, "lxml")
#print(soup.prettify())

name = soup.select_one(selector="#productTitle").getText()
name = name.strip()
#print(name)


price = soup.select_one(selector="#priceblock_dealprice").getText()

price = price[1:]

#print(price)




def get_link_data(url):
	headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
	"Accept-Language" : "en",

	}

	r = requests.get(url, headers = headers)
	soup = BeautifulSoup(r.text, "lxml")
	#print(soup.prettify())

	name = soup.select_one(selector="#productTitle").getText()
	name = name.strip()


	price = soup.select_one(selector="#priceblock_dealprice").getText()
	price = ast.literal_eval(price[2:])

	return name, price

print(get_link_data(url))
