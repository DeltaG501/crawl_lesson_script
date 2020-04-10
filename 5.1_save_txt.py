import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com/'
headers = {'User-Agent': 'Mozilla/5.O (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
r = requests.get(url, headers=headers).text
soup = BeautifulSoup(r, 'html.parser')
print(soup.prettify())
# # item = soup.select('.qrcode-text .title').text()
# question = soup.head.title.get_text()
# file = open('explore.txt', 'a', encoding='utf-8')
# file.write(question)
# file.write('\n' + '=' *50 + '\n')
# file.close()