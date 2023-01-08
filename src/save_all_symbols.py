import MetaTrader5 as mt5
from MT5functions import MT5
import csv

def save_all_symbols():
    MT5.initialize()

    all_symbols_info = mt5.symbols_get()
    all_symbol = []

    for i in all_symbols_info:
        all_symbol.append(i.name)
    print(len(all_symbol))
    print(all_symbol)

    with open('src/data/all_symbols.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(all_symbol)
        f.close()

save_all_symbols()