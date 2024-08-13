import re
import requests
from bs4 import BeautifulSoup

class CoinMarketCap:
    def __init__(self, url):
        self.url = url
        
    def get_bitcoin_price(self) -> str:        
        # Requisição HTTP para a página
        response = requests.get(self.url)
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Cria o objeto BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontra o elemento que contém o preço
            price_element = soup.find('div', class_='sc-65e7f566-0 DDohe flexStart alignBaseline')
            
            if price_element:
                # Extrai o texto do elemento e remove espaços extras
                price = price_element.get_text(strip=True)
                return price
            else:
                return "Não foi possível encontrar o preço do Bitcoin."
        else:
            return "Falha ao acessar o site."
