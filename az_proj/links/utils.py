import requests
import lxml
from bs4 import BeautifulSoup
import ast
import re



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


	price = soup.select_one(selector="#priceblock_ourprice").getText()
	#price = ast.literal_eval(price[2:])
	parsed_value = re.sub(r'\,', '', price)
	price = float(parsed_value[2:])
	print(price)

	return name, price


