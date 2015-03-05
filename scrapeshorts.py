import requests
import bs4

response = requests.get('http://www.bearbottomclothing.com/shorts-s/1817.htm')
soup = bs4.BeautifulSoup(response.text)

for span in soup.find_all('span'):
	print(span.get_text())

for b in soup.find_all('b'):
	print(b.get_text())
