import MetaTrader5 as mt5
import datetime as dt
import pandas as pd
from MT5functions import MT5


    
# ===============================================================================================
# ===============================================================================================
# ===============================================================================================
#                  --- STRATEGIES FUNCTION ---
# ===============================================================================================
# ===============================================================================================
# ===============================================================================================




# ===============================================================================================
# ESTRATEGIA DE DESAGIO - REVER SE FAZ SENTIDO, NUNCA TESTADO DE VERDADE
# ===============================================================================================

class StrategiesFunctions():

    def pct_change_close(symbol, timeframe):

        lastclose = MT5.get_rates(symbol, number_of_candles = 2, timeframe = timeframe).close[-2]
        lasttick = mt5.symbol_info_tick(symbol).bid

        pct_change = (lasttick - lastclose) / lastclose * 100

        return pct_change

    def pct_strategy_buy_low(symbol, pct_goal, checker, lot, deviation, time_now, timeframe, order, time_close, comment='python script'):

        pct_change = MT5.pct_change_close(symbol, timeframe)

        print(pct_change)
        print(pct_goal)
        print(pct_change <= pct_goal)

        if pct_change <= pct_goal and checker == 0:

            checker = 1

            buy_order = MT5.buy_market(symbol, lot, deviation, comment)

            print(buy_order)

            if timeframe == mt5.TIMEFRAME_M1:
                min = 0
            elif timeframe == mt5.TIMEFRAME_M5:
                min = 4
            elif timeframe == mt5.TIMEFRAME_M15:
                min = 14
            elif timeframe == mt5.TIMEFRAME_M30:
                min = 29
            elif timeframe == mt5.TIMEFRAME_H1:
                min = 59
            elif timeframe == mt5.TIMEFRAME_H2:
                min = 119
            elif timeframe == mt5.TIMEFRAME_H4:
                min = 239

            time_open_candle = MT5.get_rates(symbol, number_of_candles = 1, timeframe = timeframe).index[-1].to_pydatetime()
            time_close = (time_open_candle + dt.timedelta(minutes=min, seconds=59)).time()

            print()
            print(f'Order will be closed at: {time_close}')
            print()

            return checker, buy_order, time_close

        if checker == 1 and time_now >= time_close:

            checker = 2
            close_order = MT5.close_open_buy(order, deviation = 10)

            print()
            print(close_order)
            print('Order closed')
            print()

            return checker, close_order, time_close
        
        return checker, order, time_close
    
    def pct_strategy_buy_high(symbol, pct_goal, checker, lot, deviation, time_now, timeframe, order, time_close, comment='python script'):

        pct_change = MT5.pct_change_close(symbol, timeframe)

        print(pct_change)
        print(pct_goal)
        print(pct_change >= pct_goal)

        if pct_change >= pct_goal and checker == 0:

            checker = 1

            buy_order = MT5.buy_market(symbol, lot, deviation, comment)

            print(buy_order)

            if timeframe == mt5.TIMEFRAME_M1:
                min = 0
            elif timeframe == mt5.TIMEFRAME_M5:
                min = 4
            elif timeframe == mt5.TIMEFRAME_M15:
                min = 14
            elif timeframe == mt5.TIMEFRAME_M30:
                min = 29
            elif timeframe == mt5.TIMEFRAME_H1:
                min = 59
            elif timeframe == mt5.TIMEFRAME_H2:
                min = 119
            elif timeframe == mt5.TIMEFRAME_H4:
                min = 239

            time_open_candle = MT5.get_rates(symbol, number_of_candles = 1, timeframe = timeframe).index[-1].to_pydatetime()
            time_close = (time_open_candle + dt.timedelta(minutes=min, seconds=59)).time()

            print()
            print(f'Order will be closed at: {time_close}')
            print()

            return checker, buy_order, time_close

        if checker == 1 and time_now >= time_close:

            checker = 2
            close_order = MT5.close_open_buy(order, deviation = 10)

            print()
            print(close_order)
            print('Order closed')
            print()

            return checker, close_order, time_close
        
        return checker, order, time_close
    
    def pct_strategy_sell_high(symbol, pct_goal, checker, lot, deviation, time_now, timeframe, order, time_close, comment='python script'):

        pct_change = MT5.pct_change_close(symbol, timeframe)

        if pct_change >= pct_goal and checker == 0:

            checker = 1

            sell_order = MT5.sell_market(symbol, lot, deviation, comment)

            print(sell_order)

            if timeframe == mt5.TIMEFRAME_M1:
                min = 0
            elif timeframe == mt5.TIMEFRAME_M5:
                min = 4
            elif timeframe == mt5.TIMEFRAME_M15:
                min = 14
            elif timeframe == mt5.TIMEFRAME_M30:
                min = 29
            elif timeframe == mt5.TIMEFRAME_H1:
                min = 59
            elif timeframe == mt5.TIMEFRAME_H2:
                min = 119
            elif timeframe == mt5.TIMEFRAME_H4:
                min = 239

            time_open_candle = MT5.get_rates(symbol, number_of_candles = 1, timeframe = timeframe).index[-1].to_pydatetime()
            time_close = (time_open_candle + dt.timedelta(minutes=min, seconds=59)).time()

            print()
            print(f'Order will be closed at: {time_close}')
            print()

            return checker, sell_order, time_close

        if checker == 1 and time_now >= time_close:

            checker = 2
            close_order = MT5.close_open_sell(order, deviation = 10)

            print()
            print(close_order)
            print('Order closed')
            print()

            return checker, close_order, time_close
        
        return checker, order, time_close
    
    def pct_strategy_sell_low(symbol, pct_goal, checker, lot, deviation, time_now, timeframe, order, time_close, comment='python script'):

        pct_change = MT5.pct_change_close(symbol, timeframe)

        if pct_change <= pct_goal and checker == 0:

            checker = 1

            sell_order = MT5.sell_market(symbol, lot, deviation, comment)

            print(sell_order)

            if timeframe == mt5.TIMEFRAME_M1:
                min = 0
            elif timeframe == mt5.TIMEFRAME_M5:
                min = 4
            elif timeframe == mt5.TIMEFRAME_M15:
                min = 14
            elif timeframe == mt5.TIMEFRAME_M30:
                min = 29
            elif timeframe == mt5.TIMEFRAME_H1:
                min = 59
            elif timeframe == mt5.TIMEFRAME_H2:
                min = 119
            elif timeframe == mt5.TIMEFRAME_H4:
                min = 239

            time_open_candle = MT5.get_rates(symbol, number_of_candles = 1, timeframe = timeframe).index[-1].to_pydatetime()
            time_close = (time_open_candle + dt.timedelta(minutes=min, seconds=59)).time()

            print()
            print(f'Order will be closed at: {time_close}')
            print()

            return checker, sell_order, time_close

        if checker == 1 and time_now >= time_close:

            checker = 2
            close_order = MT5.close_open_sell(order, deviation = 10)

            print()
            print(close_order)
            print('Order closed')
            print()

            return checker, close_order, time_close
        
        return checker, order, time_close



# ===============================================================================================
# STRATEGY TO OPEN AND CLOSE ORDER AT SPECIFIC TIME - WITHOUT SL AND TP
# ===============================================================================================


class Strategy_at_time():
    checker = 0
    order = []
    close_order = []
    def __init__(self, time_init, time_close, symbol, volume, deviation, buy=True, comment='python at time', magic=10001):
        self.time_init = time_init
        self.time_close = time_close
        self.symbol = symbol
        self.volume = volume
        self.deviation = deviation
        self.comment = comment
        self.buy = buy
        self.magic = magic
    
    # Open the buy or sell order
    def check_time_init(abc):
        time0 = dt.datetime.now().time().replace(microsecond=0)
        if time0 == abc.time_init and abc.checker == 0 and abc.buy == True:
            buy_order = MT5.buy_market(abc.symbol, abc.volume, abc.deviation, abc.comment, abc.magic)
            abc.checker = 1
            abc.order = buy_order
            print()
            print(buy_order)
            print()
        if time0 == abc.time_init and abc.checker == 0 and abc.buy == False:
            sell_order = MT5.sell_market(abc.symbol, abc.volume, abc.deviation, abc.comment, abc.magic)
            abc.checker = 1
            abc.order = sell_order
            print()
            print(sell_order)
            print()

    # Close the opened order
    def check_time_close(abc):
        time0 = dt.datetime.now().time().replace(microsecond=0)
        
        if time0 == abc.time_close and abc.checker == 1 and abc.buy == True:
            close_order = MT5.close_open_buy(abc.order, abc.deviation)
            abc.checker = 2
            abc.close_order = close_order
            print()
            print(close_order)
            print()
        if time0 == abc.time_close and abc.checker == 1 and abc.buy == False:
            close_order = MT5.close_open_sell(abc.order, abc.deviation)
            abc.checker = 2
            abc.close_order = close_order
            print()
            print(close_order)
            print()

# ===============================================================================================
# STRATEGY TO OPEN AND CLOSE ORDER AT SPECIFIC TIME - WITH SL AND TP
# ===============================================================================================

class Strategy_at_time_sl_tp():
    checker = 0
    order = []
    close_order = []

    def __init__(self, time_init, time_close, symbol, volume, sl, tp, deviation, buy=True, comment='python at time', magic=10002):
        self.time_init = time_init
        self.time_close = time_close
        self.symbol = symbol
        self.volume = volume
        self.sl = sl
        self.tp = tp
        self.deviation = deviation
        self.comment = comment
        self.buy = buy
        self.magic = magic
    
    # Open the buy or sell order
    def check_time_init(abc):
        time0 = dt.datetime.now().time().replace(microsecond=0)

        # Buy order type
        if time0 == abc.time_init and abc.checker == 0 and abc.buy == True:
            buy_order = MT5.buy_market_order(abc.symbol, abc.volume, abc.sl, abc.tp, abc.deviation, abc.comment, abc.magic)
            #buy_market(abc.symbol, abc.volume, abc.deviation, abc.comment)
            abc.checker = 1
            abc.order = buy_order
            print()
            print(buy_order)
            print()
        
        # Sell order type
        if time0 == abc.time_init and abc.checker == 0 and abc.buy == False:
            sell_order = MT5.sell_market_order(abc.symbol, abc.volume, abc.sl, abc.tp, abc.deviation, abc.comment, abc.magic)
            abc.checker = 1
            abc.order = sell_order
            print()
            print(sell_order)
            print()

    # Close the opened order
    def check_time_close(abc):
        time0 = dt.datetime.now().time().replace(microsecond=0)
        
        # Close Buy order
        if time0 == abc.time_close and abc.checker == 1 and abc.buy == True:
            close_order = MT5.close_open_buy(abc.order, abc.deviation)
            abc.checker = 2
            abc.close_order = close_order
            print()
            print(close_order)
            print()

        # Close Sell order
        if time0 == abc.time_close and abc.checker == 1 and abc.buy == False:
            close_order = MT5.close_open_sell(abc.order, abc.deviation)
            abc.checker = 2
            abc.close_order = close_order
            print()
            print(close_order)
            print()


class Strategy_at_sl():
    checker = 0
    order = []
    close_order = []

    def __init__(self, strat_at_open, comment='python at time', magic=10003):
        self.strat_at_open = strat_at_open
        self.comment = comment
        self.magic = magic
    
    # Open the buy or sell order
    def check_time_init(abc):
        time0 = dt.datetime.now().time().replace(microsecond=0)
        delta = MT5.delta_from_open(abc.strat_at_open.symbol)
        #No_orders, orders = MT5.check_positions(abc.strat_at_open.symbol)

        if time0 > abc.strat_at_open.time_init and time0 < abc.strat_at_open.time_close and abc.strat_at_open.checker == 1 and delta >= abc.strat_at_open.sl and abc.strat_at_open.buy == False:
            buy_order = MT5.buy_market(abc.strat_at_open.symbol, abc.strat_at_open.volume, abc.strat_at_open.deviation, abc.comment, abc.magic)
            abc.checker = 1
            abc.order = buy_order
            print()
            print(buy_order)
            print()
        if time0 > abc.strat_at_open.time_init and time0 < abc.strat_at_open.time_close and abc.strat_at_open.checker == 1 and delta <= -abc.strat_at_open.sl and abc.strat_at_open.buy == True:
            sell_order = MT5.sell_market(abc.strat_at_open.symbol, abc.strat_at_open.volume, abc.strat_at_open.deviation, abc.comment, abc.magic)
            abc.checker = 1
            abc.order = sell_order
            print()
            print(sell_order)
            print()

    # Close the opened order
    def check_time_close(abc):
        time0 = dt.datetime.now().time().replace(microsecond=0)
        
        if time0 == abc.strat_at_open.time_close and abc.checker == 1 and abc.strat_at_open.buy == False:
            close_order = MT5.close_open_buy(abc.order, abc.strat_at_open.deviation)
            abc.checker = 2
            abc.close_order = close_order
            print()
            print(close_order)
            print()
        if time0 == abc.strat_at_open.time_close and abc.checker == 1 and abc.strat_at_open.buy == True:
            close_order = MT5.close_open_sell(abc.order, abc.strat_at_open.deviation)
            abc.checker = 2
            abc.close_order = close_order
            print()
            print(close_order)
            print()


# ===============================================================================================
# STRATEGY TO OPEN ORDER AT MARKET OPENING HOUR WITH SL ONLY
# ===============================================================================================

class Strategy_at_opening():
    checker = 0
    buy_order = []
    sell_order = []
    close_buy_order = []
    close_sell_order = []
    buy = []

    def __init__(self, time_open, time_close, symbol, volume, sl, deviation, comment = 'OpeningStrategy', magic=10004):
        self.time_open = time_open
        self.time_close = time_close
        self.symbol = symbol
        self.volume = volume
        self.sl = sl
        self.deviation = deviation
        self.comment = comment
        self.magic = magic
    
    def check_time_init(abc):
        time0 = dt.datetime.now().time().replace(microsecond=0)

        if time0 == abc.time_open and abc.checker == 0:

            abc.sell_order = MT5.sell_market_order_sl(abc.symbol, abc.volume, abc.sl, abc.deviation, abc.comment, abc.magic)
            abc.buy_order  = MT5.buy_market_order_sl(abc.symbol, abc.volume, abc.sl, abc.deviation, abc.comment, abc.magic)

            abc.checker = 1


    def check_time_close(abc):
        time0 = dt.datetime.now().time().replace(microsecond=0)

        if time0 == abc.time_close and abc.checker == 1:
            abc.close_buy_order = MT5.close_open_buy(abc.buy_order, abc.deviation)
            abc.close_sell_order = MT5.close_open_sell(abc.sell_order, abc.deviation)
            
            abc.checker = 2

            print()
            print(abc.close_buy_order)
            print()
            print(abc.close_sell_order)
            print()
