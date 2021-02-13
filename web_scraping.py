import requests
from bs4 import BeautifulSoup

url_summary = 'https://guialinux.uniriotec.br'

# Requesição GET na url da página
req_get = requests.get(url_summary)

soup = BeautifulSoup(req_get.content, 'html.parser')

commands = [link.find('a').text for link in soup.find_all('dt')]

links = [link.find('a').attrs['href'] for link in soup.find_all('dt')]

Summary = [item.text for item in soup.find_all('dd')]

join_lists = list(zip(links, commands, Summary))

# print(len(link), len(comando))

for item in join_lists:
    print(item)


print(len(join_lists))
