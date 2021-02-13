import requests
from bs4 import BeautifulSoup

url_summary = 'https://guialinux.uniriotec.br'

# Requesição GET na url da página
req_get = requests.get(url_summary)

# Converte o html em obj python para manipulação
soup = BeautifulSoup(req_get.content, 'html.parser')

# Procura por todas as tags 'td', após tag 'a' de cada uma e retira o texto
commands = [link.find('a').text for link in soup.find_all('dt')]

# Procura por todas as tags 'td', após, tag 'a' de cada uma e retira o link(href)
links = [link.find('a').attrs['href'] for link in soup.find_all('dt')]

# Procura por todas as tags 'dd' e retira o texto contido em cada uma delas
overview = [item.text for item in soup.find_all('dd')]


join_lists = list(zip(commands, overview, links))

# print(len(link), len(comando))

for item in join_lists:
    print(item)


print(len(join_lists))
