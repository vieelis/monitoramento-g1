import requests
from bs4 import BeautifulSoup
import pandas as pd

def monitorar_sub_urls(soup):
    """Função para monitorar e coletar manchetes das sub-URLs."""
    
    # Encontrando links das sub-URLs
    sub_urls = soup.find_all('a', {'class': 'feed-post-body-title'})
    
    # Lista para armazenar as URLs
    urls_extracao = []
    
    for link in sub_urls:
        sub_url = link.get('href')
        urls_extracao.append(sub_url)
    
    # Lista para armazenar manchetes das sub-URLs
    lista_manchetes_sub = []
    
    # Fazendo a requisição em cada sub-URL e coletando manchetes
    for sub_url in urls_extracao:
        response_sub = requests.get(sub_url)
        soup_sub = BeautifulSoup(response_sub.content, 'html.parser')
        
        # Coletando manchetes da sub-URL
        manchetes_sub = soup_sub.find_all('a', {'class': 'feed-post-link'})
        
        for manchete in manchetes_sub:
            lista_manchetes_sub.append(manchete.get_text())
    
    # Exibindo as manchetes das sub-URLs
    for idx, manchete in enumerate(lista_manchetes_sub, start=1):
        print(f"Sub-URL Manchete {idx}: {manchete}")
    
    # Salvando as manchetes das sub-URLs em um arquivo CSV
    df_manchetes_sub = pd.DataFrame(lista_manchetes_sub, columns=['Manchete'])
    df_manchetes_sub.to_csv('manchetes_sub_urls.csv', index=False)
    print("Manchetes das sub-URLs salvas em 'manchetes_sub_urls.csv'")


