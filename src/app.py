__author__ = 'Hunter Files'

import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.walmart.com/ip/Racing-Style-Reclining-Ergonomic-Gaming-Chair/164051334?wpa_bd=1574373455979&wpa_pg_seller_id=0B891523724B4CB68C351F0057C3AA46&wpa_ref_id=dc1e97f581624d353495683e84f037d4&wpa_aux_info=&wpa_tag=&wpa_pos=3&wpa_plmt=1145x1145_T-C-IG_TI_1-2_HL-INGRID-GRID-NY&wpa_aduid=6ca795ce-08b4-4297-89f5-65692d5dba34&wpa_pg=search&wpa_pg_id=gaming%20chair&wpa_st=gaming%2Bchair&wpa_tax=4044_103150&wpa_bucket=__bkt__")


# <span class="price-characteristic" itemprop="price" content="129.99">129</span>
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "price-characteristic", "itemprop": "price"})
stringPrice = element.text.strip()  # "$129.00"

priceWithoutSymbol = stringPrice[:] # [1:]"129.00" to strip off "$" if it had it

price = float(priceWithoutSymbol)
# you can buy if it is lesser than $200.00
print("You can buy the chair" if price < 200.0 else "You can't buy this chair")

# if you set it equal to stringPrice exactly, it copies the place in memory
print(float(priceWithoutSymbol))
