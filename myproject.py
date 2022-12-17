import requests
from bs4 import BeautifulSoup

res=[]

products=requests.get("https://www.amazon.eg/s?k=laptop&crid=2BYMC96CZV4TI&sprefix=l%2Caps%2C247&ref=nb_sb_ss_ts-doa-p_1_1")
src=products.content
soup=BeautifulSoup(src , "html.parser")

products=soup.find_all("div", 'a-section a-spacing-base')


for i in range(len(products)):
    res.append(products[i].text)

    print(products[i].text)

