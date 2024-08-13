import re
from mail_config.mail import Mail
from web_scraping.webscraping_bovespa import Bovespa
from web_scraping.webscraping_coinmarketcap import CoinMarketCap
from const import *
import os
from dotenv import load_dotenv

load_dotenv()

mail_from = os.getenv("MAIL_FROM")
mail_password = os.getenv("MAIL_PASSWORD")

get_values_from_bovespa = Bovespa(BOVESPA_URL, CSV_PATH)

mail = Mail(MAIL_FROM, MAIL_PASSWORD)

get_bitcoin_value = CoinMarketCap(COINMARKETCAP_URL)
price = get_bitcoin_value.get_bitcoin_price()


if price == 'Não foi possível encontrar o preço do Bitcoin.' or 'Falha ao acessar o site.':
    subject = 'ERRO: Não foi possível coletar o preço do Bitcoin.'
    body = '''Olá
    Não foi possível coletar o preço do Bitcoin. 
    Tente novamente mais tarde ou verifique se houve mudanças no site.'''
else:
    price = re.sub(r'[^0-9,.]', '', price)
    subject = 'Atualização de preço do Bitcoin'
    body = f'''Olá
    O preço do Bitcoin hoje é R${price[0:price.index('.')]}.'''