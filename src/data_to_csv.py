import MetaTrader5 as mt5
from MT5functions import MT5
import csv

MT5.initialize()

# Input Parameters

# Get list with all Symbols from MT5 - change file for less symbols or write symbols list below
with open('src/data/all_symbols.csv', newline='') as f:
    reader = csv.reader(f)
    symbols = list(reader)[0]
#symbols = ['Ger40', 'HKInd', 'Usa500', 'UsaInd', 'UsaTec', 'Bra50', 'MinDolDec22']

# Timeframe for naming and for MetaTrader reference
#tfs     = ['M15', 'M30', 'H1', 'H2', 'H4', 'H6', 'D1', 'W1']
#timeframes = [mt5.TIMEFRAME_M15, mt5.TIMEFRAME_M30, mt5.TIMEFRAME_H1, mt5.TIMEFRAME_H2, mt5.TIMEFRAME_H4, mt5.TIMEFRAME_H6, mt5.TIMEFRAME_D1, mt5.TIMEFRAME_W1]

tfs     = ['M5','M15', 'M30', 'H1', 'D1']
timeframes = [mt5.TIMEFRAME_M5, mt5.TIMEFRAME_M15, mt5.TIMEFRAME_M30, mt5.TIMEFRAME_H1, mt5.TIMEFRAME_D1]

number_of_data = 1000000

for symbol in symbols:
    i = 0

    for timeframe in timeframes:
        # Get rates from MetaTrader
        rates = MT5.get_rates(symbol, number_of_data, timeframe)
        # Save rates in a .csv file
        rates.to_csv(f'X:\market\Data_MT5\{tfs[i]}_{symbol}.csv')
        # Print file path for reference
        print(f'Data_MT5/{tfs[i]}_{symbol}.csv')
        i += 1


MT5.shutdown()
