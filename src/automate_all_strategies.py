import datetime as dt
from MT5functions import MT5, Strategy_at_opening, Strategy_at_time_sl_tp, Strategy_at_sl

if __name__ == '__main__':

    # Initialize MT5 terminal connection
    MT5.initialize()

    # ====================Strategies===================
    # =================================================


    # ====================Strategy 1=================== 
    # Open an orders at a defined time with TP and SL,
    # if the order is still opened, it is closed at a defined time
    # Additional strategy - if it hits SL an opposite order is opened

    HKInd_0230_15 = Strategy_at_time_sl_tp(dt.time(1,29,59), dt.time(1,45,0), 'HK50.cash', volume=16.0, sl=6000, tp=3000, deviation=100, buy=True, comment='HKInd 02:30_open')
    HKInd_0230_15_stop_strategy = Strategy_at_sl(HKInd_0230_15, comment = 'HKInd 02:30_stop')
    Ger40_0900_15  = Strategy_at_time_sl_tp(dt.time(7,59,59), dt.time(8,15,0), 'GER40.cash', volume=8.0, sl=1500, tp=1000, deviation=100, buy=True, comment='Ger40 09:00_open')
    UsaTec_1530_15 = Strategy_at_time_sl_tp(dt.time(14,29,59), dt.time(14,45,0), 'US100.cash', volume=8.0, sl=1500, tp=1000, deviation=00, buy=False, comment='UsaTec 14:30_open')

    # Trades list
    trades_strategy_1 = [HKInd_0230_15, 
                         Ger40_0900_15,
                         UsaTec_1530_15
                        ]
    trades_sl = [HKInd_0230_15_stop_strategy]



    # ====================Strategy 2=================== 
    # Open two orders at a defined time with only SL,
    # order closed at a definied time

    HKInd1 = Strategy_at_opening(dt.time(1,29,59), dt.time(1,45,0), 'HK50.cash', volume=80.0, sl=1200, deviation=100, comment = 'HKInd opening 15M sl=500')
    HKInd2 = Strategy_at_opening(dt.time(1,29,59), dt.time(2,0,0), 'HK50.cash', volume=80.0, sl=1200, deviation=100, comment = 'HKInd opening 30M sl=500')
    UsaInd = Strategy_at_opening(dt.time(14,29,59), dt.time(14,45,0), 'US30.cash', volume=10.0, sl=500, deviation=100, comment = 'UsaInd opening 15M sl=500')

    # Trades list
    trades_strategy_2 = [HKInd1, HKInd2, UsaInd]

    while True:

        for trade in trades_strategy_1:
            trade.check_time_init()
            trade.check_time_close()
        
        for trade in trades_sl:
            trade.check_time_init()
            trade.check_time_close()

        for trade in trades_strategy_2:
            trade.check_time_init()
            trade.check_time_close()
        

        MT5.check_time_shutdown(dt.time(14,45,30))