import os
from datetime import datetime

BOVESPA_URL = 'https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br'
COINMARKETCAP_URL = 'https://coinmarketcap.com/currencies/bitcoin/'

CSV_PATH = os.path.join('data_output', f'{datetime.now().strftime("%d/%m/%Y")}.csv')
