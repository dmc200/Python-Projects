from bs4 import BeautifulSoup
import requests
import os

os.chdir('c:\\users\\dchrie504\\Desktop\\Tutorial')

html = requests.get('http://coreyms.com').text
soup = BeautifulSoup(html, 'lxml')
articles = soup.find_all('article')

filename = 'CoreysBlogs.csv'

f = open(filename, 'w')
header = 'Link' + ',' + 'Headline' + ',' + 'Summary' + '\n'
f.write(header)

for article in articles:

	try:
		headline = article.h2.a.text.replace(',','|')

		summary = article.find('div', class_='entry-content').p.text.replace(',','|')

		vid_src = article.find('iframe', class_='youtube-player')

		vid_id = vid_src['src'].split('/')[4].split('?')[0]

		yt_link = f'https://youtube.com/watch?v={vid_id}'

		
	except Exception as e:
		yt_link = None
		summary = None
		headline = None

	f.write(yt_link + ',' + headline + ',' + summary + '\n')

f.close()