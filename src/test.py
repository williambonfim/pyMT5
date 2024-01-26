from datetime import datetime
import pytz

timezone = pytz.timezone("Etc/UTC") 

utc = datetime(2020,1,10, tzinfo=timezone)
print(utc)


from_date = datetime.now()
print(from_date)

import MetaTrader5 as mt5
from MT5functions import MT5
MT5.initialize()

symbols=mt5.symbols_get()
print('Symbols: ', len(symbols))
count=0
# display the first five ones
for s in symbols:
    count+=1
    print("{}. {}".format(count,s.name))
    if count==120: break
print()


'''rates = MT5.get_rates('USA500', number_of_candles = 100, timeframe = mt5.TIMEFRAME_M1)
print(rates)'''

timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, datetime.now(), 10)
print(rates)