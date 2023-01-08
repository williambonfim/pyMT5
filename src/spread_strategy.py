import MetaTrader5 as mt5
from MT5functions import MT5
import pandas as pd

MT5.initialize()

symbols = [['Ger40', 'Ger40Mar23'], 
           ['Usa500', 'Usa500Mar23'], 
           ['UsaInd', 'UsaIndMar23'], 
           ['UsaTec', 'UsaTecMar23'], 
           ['Bra50', 'Bra50Feb23']]

df = pd.DataFrame(columns = ['ticker', 'continuous', 'future', 'delta'])

for pair in symbols:
    rates = [pair[0]]
    
    for symbol in pair:
        price = MT5.get_rates(symbol, 1, mt5.TIMEFRAME_M15)['close'].iat[-1]
        rates.append(price)

    delta = rates[2] - rates[1]
    rates.append(delta)

    rates = pd.DataFrame([rates], columns=['ticker', 'continuous', 'future', 'delta'])
    df = pd.concat([df, rates])

df.set_index('ticker', inplace=True)
print(df)
