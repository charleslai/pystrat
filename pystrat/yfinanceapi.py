#yfinanceapi.py
#Charles J. Lai
#September 30, 2013
import urllib

"""
==============
yfinanceapi.py
==============

The following is a module containing a Python API into Yahoo Finance RESTful
API for getting stock ticker information in CSV format. It includes an umbrella
function call that returns a hash table of various relevant stock information
as well as individual methods that return a single integer or string of relevant
information. This module does not provide support for simultaneously getting data
for 2 or more stock tickers.

Common Parameters
-----------------
symbol = stock ticker symbol for a given security is string form (ex. 'goog')

Methods
-------
get_all(symbol)


"""
def __fetch(symbol, parameter):
    """
    Returns: List of values parsed from the Yahoo finance csv object.

    First, the function reads from a Yahoo finance csv url using an
    http request from urllib.urlopen().

    Values of the csv object are parsed and placed into a list in the
    order of the "f=parameter" given. For example if "f=ns" then the
    name of the security is placed into the list first and followed
    by the symbol.
    """
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, parameter)
    #Parse the values an place into a list
    return urllib.urlopen(url).read().strip().strip('"')

#=========================================================================
#                  Commonly Retrieved Values Function
#=========================================================================
def get_all(symbol):
    """
    Returns: A hash table/dictionary of values.

    Gets commonly used data for a specific security and places it into a
    hash table of values. Look up keys are strings such as 'symbol', 'name'
    or 'dividend_yield'. A full list of fetched information can be gleaned
    from the following source code. 
    """
    values = __fetch(symbol, 'snxopl1c1ghva2j1dyjkm3m4erj4').split(',')
    stock_data = {}
    stock_data['symbol'] =                        values[0]
    stock_data['name'] =                          values[1]
    stock_data['exchange'] =                      values[2]
    stock_data['open'] =                          values[3]
    stock_data['prev_close'] =                    values[4]
    stock_data['price'] =                         values[5]
    stock_data['change'] =                        values[6]
    stock_data['days_low'] =                      values[7]
    stock_data['days_high'] =                     values[8]
    stock_data['volume'] =                        values[9]
    stock_data['avg_daily_volume'] =              values[10]
    stock_data['market_cap'] =                    values[11]
    stock_data['dividend_per_share'] =            values[12]
    stock_data['dividend_yield'] =                values[13]
    stock_data['52_week_low'] =                   values[14]
    stock_data['52_week_high'] =                  values[15]   
    stock_data['50_day_ma'] =                     values[16]
    stock_data['200_day_ma'] =                    values[17]
    stock_data['earnings_per_share'] =            values[18]
    stock_data['price_earnings_ratio'] =          values[19]
    stock_data['ebitda'] =                        values[20]
    return stock_data

#=========================================================================
#                       Historical Price Function
#=========================================================================
def get_historical_prices(symbol, start_date, end_date):
    """
    Returns: A list of historical prices for the given ticker symbol and 
    range of dates. 

    Preconditions: start_date and end_date are in 'YYYYMMDD' format.
    """
    url = 'http://ichart.yahoo.com/table.csv?s=%s&' % symbol + \
          'd=%s&' % str(int(end_date[4:6]) - 1) + \
          'e=%s&' % str(int(end_date[6:8])) + \
          'f=%s&' % str(int(end_date[0:4])) + \
          'g=d&' + \
          'a=%s&' % str(int(start_date[4:6]) - 1) + \
          'b=%s&' % str(int(start_date[6:8])) + \
          'c=%s&' % str(int(start_date[0:4])) + \
          'ignore=.csv'
    days = urllib.urlopen(url).readlines()
    data = [day[:-2].split(',') for day in days]
    return data 

#=========================================================================
#                   Individual Data Mining Functions
#=========================================================================
def get_symbol(symbol):
    """
    Returns: A one-dimensional list containing the string representation
    of the ticker symbol for a given security.

    (Kind of redundant but here in order for the Yahoo Finance API to be
    fairly complete)
    """
    return __fetch(symbol, 's')


def get_name(symbol):
    """
    Returns: A one-dimensional list containing the string representation
    of the name for a given security.
    """
    return __fetch(symbol, 'n')


def get_open(symbol):
    """
    Returns: A one-dimensional list containing the string representation
    of the opening price for a given security.
    """
    return __fetch(symbol, 'o')
    

def get_prev_close(symbol):
    return __fetch(symbol, 'p')

def get_price(symbol): 
    return __fetch(symbol, 'l1')


def get_change(symbol):
    return __fetch(symbol, 'c1')
    
    
def get_volume(symbol): 
    return __fetch(symbol, 'v')


def get_avg_daily_volume(symbol): 
    return __fetch(symbol, 'a2')
    
    
def get_stock_exchange(symbol): 
    return __fetch(symbol, 'x')
    
    
def get_market_cap(symbol):
    return __fetch(symbol, 'j1')
   
   
def get_book_value(symbol):
    return __fetch(symbol, 'b4')


def get_ebitda(symbol): 
    return __fetch(symbol, 'j4')
    
    
def get_dividend_per_share(symbol):
    return __fetch(symbol, 'd')


def get_dividend_yield(symbol): 
    return __fetch(symbol, 'y')
    
    
def get_earnings_per_share(symbol): 
    return __fetch(symbol, 'e')


def get_52_week_high(symbol): 
    return __fetch(symbol, 'k')
    
    
def get_52_week_low(symbol): 
    return __fetch(symbol, 'j')


def get_50day_moving_avg(symbol): 
    return __fetch(symbol, 'm3')
    
    
def get_200day_moving_avg(symbol): 
    return __fetch(symbol, 'm4')
    
    
def get_price_earnings_ratio(symbol): 
    return __fetch(symbol, 'r')


def get_price_earnings_growth_ratio(symbol): 
    return __fetch(symbol, 'r5')


def get_price_sales_ratio(symbol): 
    return __fetch(symbol, 'p5')
    
    
def get_price_book_ratio(symbol): 
    return __fetch(symbol, 'p6')
       
       
def get_short_ratio(symbol): 
    return __fetch(symbol, 's7')
