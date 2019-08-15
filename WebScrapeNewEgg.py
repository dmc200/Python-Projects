from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'


uClient = uReq(my_url)

#Return Raw html from read() method. 
page_html = uClient.read()
uClient.close()

#Create Soup object out of html.
page_soup = soup(page_html)

# Find all containers with specified class type.
containers = page_soup.findAll('div', {'class','item-container'})

filename = 'GPU_Webscraped.csv'
f = open(filename, 'w')
header = 'brand,product,shipping' + '\n'
f.write(header)

for container in containers:
    # Get Brand Name
    divWithInfo = container.find('div',{'class','item-info'})
    brand = divWithInfo.a.img['title']
    # Get Item Title
    item_title = container.find('a',{'class':'item-title'})
    product = item_title.text.replace(',', '|')
    # Get Shipping Price
    shipping = container.find('li',{'class':'price-ship'})
    shipping = shipping.text.replace('Shipping','').strip()
    f.write(brand + ',' + product + ',' + shipping + '\n')


f.close()
    
