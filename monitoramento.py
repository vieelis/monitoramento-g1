import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site G1
url = 'https://g1.globo.com/'

# Fazendo a requisição ao site
response = requests.get(url)
if response.status_code == 200:
    print("Conexão bem-sucedida!")
else:
    print(f"Erro ao acessar o site: {response.status_code}")

# Parsing do conteúdo HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrando as manchetes principais (tags <a> com classe específica)
manchetes = soup.find_all('a', {'class': 'feed-post-link'})

# Lista para armazenar as manchetes
lista_manchetes = [manchete.get_text() for manchete in manchetes]

# Exibindo as manchetes
for idx, manchete in enumerate(lista_manchetes, start=1):
    print(f"{idx}. {manchete}")

# Salvando as manchetes em um arquivo CSV
df_manchetes = pd.DataFrame(lista_manchetes, columns=['Manchete'])
df_manchetes.to_csv('manchetes_g1.csv', index=False)
print("Manchetes salvas em 'manchetes_g1.csv'")


