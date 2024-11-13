import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/instant_pot/"
target_price = 100
live_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# Practice
response = requests.get(URL, headers=header)

# soup = BeautifulSoup(response.text, "html.parser")
# product_price = float(soup.find(class_="aok-offscreen").getText().split("$")[1])
# product_name = soup.find(id="productTitle").getText().strip()

# if product_price < target_price:
#     print(f"Subject: Amazon Price Alert!\nMessage: {product_name} is now ${product_price}\n {URL}")

response_live = requests.get(live_URL, headers=header)

soup = BeautifulSoup(response_live.text, "html.parser")

product_price = float(soup.find(class_="aok-offscreen").getText().split("$")[1])
print(product_price)
product_name = soup.find(id="productTitle").getText().strip()
print(product_name)

if product_price < target_price:
    print(f"Subject: Amazon Price Alert!\nMessage: {product_name} is now ${product_price}\n {live_URL}")