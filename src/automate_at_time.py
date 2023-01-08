import datetime as dt
from MT5functions import MT5, Strategy_at_time

if __name__ == '__main__':

    # Initialize the MT5 terminal connection
    MT5.initialize()

    # Add definied strategies 
    # OPEN AND CLOSE AN ORDER AT A DEFINIED TIME
    HKInd_0730_30 = Strategy_at_time(dt.time(6,30,0), dt.time(7,0,0), 'HKInd', 0.30, 100, buy=True, comment='HKInd 07:30')

    trades = [HKInd_0730_30
            ]

    
    while True:
        
        for trade in trades:
            trade.check_time_init()
            trade.check_time_close()

        MT5.check_time_shutdown(dt.time(7,1,0))


