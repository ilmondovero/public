# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:05:28 2024

@author: Stagista01
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Lista degli indici
indici = {
    '^GSPC': 'S&P 500',
    '^IXIC': 'NASDAQ',
    '^DJI': 'Dow Jones',
    '^RUT': 'Russell 2000',
    '^FTSE': 'FTSE 100',
    '^N225': 'Nikkei 225',
    '000300.SS': 'CSI 300',
    '^NSEI': 'Nifty 50',
    '^STOXX': 'EURO STOXX 600',
    'FTSEMIB.MI': 'FTSE MIB',
    '^GDAXI': 'DAX 40'
}

# Definizione del periodo
end_date = datetime.now()
start_date = end_date - timedelta(days=16)  # Ultime due settimane

# Scarica i dati settimanali
data = yf.download(list(indici.keys()), start=start_date, interval='1wk')['Adj Close'].rename(columns=indici)

# Calcola i rendimenti settimanali e formatta in percentuale
rendimenti = data.pct_change().dropna().T.map(lambda x: f'{x*100:.2f}%' if pd.notnull(x) else '-')

# Formatta l'indice di data nel formato dd/mm/yyyy
rendimenti.columns = rendimenti.columns.strftime('%d/%m/%Y')

# Ordina la tabella secondo l'ordine del dizionario
rendimenti = rendimenti.loc[indici.values()]
print(rendimenti)
