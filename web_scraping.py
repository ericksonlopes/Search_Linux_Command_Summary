import requests
from bs4 import BeautifulSoup

url_summary = 'https://guialinux.uniriotec.br'

# Requesição GET na url da página
req_get = requests.get(url_summary)

# C
soup = BeautifulSoup(req_get.content, 'html.parser')

commands = [code.find('a').attrs['href'] for code in soup.find_all('dt')]

comando = soup.find_all('dd')

print(len(commands), len(comando))

join_list = list(zip(comando, commands))

for item in join_list:
    print(item[0])



