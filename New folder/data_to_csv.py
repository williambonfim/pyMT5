import MetaTrader5 as mt5
from MT5functions import MT5
import csv

MT5.initialize()

# Input Parameters
csv_file = 'activtrades_symbols'

# Timeframe for naming and for MetaTrader reference
tfs     = ['M5','M15', 'M30', 'H1', 'H12', 'D1']
tfs = ['M5']
timeframes = [mt5.TIMEFRAME_M5, mt5.TIMEFRAME_M15, mt5.TIMEFRAME_M30, mt5.TIMEFRAME_H1, mt5.TIMEFRAME_H12, mt5.TIMEFRAME_D1]
timeframes = [mt5.TIMEFRAME_M5]

number_of_data = 150000 #1000000

# Get list with all Symbols from MT5 - change file for less symbols or write symbols list below
with open(f'pyMT5/New Folder/data/{csv_file}.csv', newline='') as f:
    reader = csv.reader(f)
    symbols = list(reader)[0]

total = len(symbols)
print(f'Total No. of symbols: {total}')

for symbol in symbols:
    i = 0
    print()
    print(symbol)
    for timeframe in timeframes:
        # Get rates from MetaTrader
        rates = MT5.get_rates(symbol, number_of_data, timeframe)
        # Save rates in a .csv file
        rates.to_csv(f'Z:/MT5/Market/pyMT5/New folder/MT5_data/{tfs[i]}_{symbol}.csv')
        # Print file path for reference
        print(f'Data_MT5/{tfs[i]}_{symbol}.csv')
        i += 1
    total = total-1
    print(f'{total} remaining symbols...')

MT5.shutdown()