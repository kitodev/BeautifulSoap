import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase
i=1
def make_soup(url):
    thepage= urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

SKU = input()

soup = make_soup("https://www.neutrik.com/en/product/" + SKU)

for texta in soup.findAll('div',{"class":"editor-style"}):
        print(texta.find('p').text)

for img in soup.findAll('img',{'alt': 'NADB15FF'}):
    temp=img.get('src')
    if temp[:1]=="/":
        image = "https://www.neutrik.com/uploads/media" + temp
    else:
        image = temp

    print(image)

    
    nametemp = img.get('alt')
    if len(nametemp)==0:
        filename=str(i)
        i=i+1
    else:
        filename=nametemp

    imagefile = open(filename + ".jpg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()