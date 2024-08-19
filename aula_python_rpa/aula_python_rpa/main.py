import re
from web_scraping.webscraping_bovespa import Bovespa
from web_scraping.webscraping_coinmarketcap import CoinMarketCap
from const import *
'''
get_values_from_bovespa = Bovespa(BOVESPA_URL, CSV_PATH)
get_values_from_bovespa.get_values_b3()
'''
get_bitcoin_value = CoinMarketCap(COINMARKETCAP_URL)
price = get_bitcoin_value.get_bitcoin_price()

if price == ('Não foi possível encontrar o preço do Bitcoin.' or 'Falha ao acessar o site.'):
    print('ERRO: Não foi possível coletar o preço do Bitcoin.')
    print(f'Não foi possível coletar o preço do Bitcoin.\nTente novamente mais tarde ou verifique se houve mudanças no site.\nError: {price}')
else:
    price = re.sub(r'[^0-9,.]', '', price)
    print('Atualização de preço do Bitcoin')
    print(f'O preço do Bitcoin hoje é R${price[0:price.index('.')]}.')
    