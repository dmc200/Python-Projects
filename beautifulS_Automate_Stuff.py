import bs4, requests


def getAmazonPrice(proURL):
    res = requests.get(proURL)
    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
    return elems[0].text
    



price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?crid=PUEMF18WKA6Z&keywords=automate+the+boring+stuff+with+python&qid=1554682451&s=gateway&sprefix=automate+%2Caps%2C146&sr=8-1')
print('The price is ' + price)
