import bs4, requests

def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#price_inside_buybox')
    price = elems[0].text.strip()
    return price



    







price = getAmazonPrice('https://www.amazon.com/Brushed-Oyster-Stainless-Bracelet-Seiko/dp/B00CHZ9B60/ref=pd_sim_241_3/146-2252472-4501140?_encoding=UTF8&pd_rd_i=B00CHZ9B60&pd_rd_r=0ea0a755-27c9-11e9-bd58-413f05c8b3cb&pd_rd_w=8ZDUT&pd_rd_wg=vmrEe&pf_rd_p=5ac5df22-d3ad-42b5-bda0-fa347f66dbf5&pf_rd_r=6X087A99TJK3B0K5270C&psc=1&refRID=6X087A99TJK3B0K5270C')
print("The price is, " + price)
