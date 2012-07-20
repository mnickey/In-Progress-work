#!/usr/bin/python2.7
'''
Created on Jul 18, 2012
Create a fictional stock parser that combines several lists into a dictionary.
Use stock symbols, number of shares, purchase price and current price for the user to select as their filter.
Display results with the users selection as the key followed by the rest of the items as the value.
@author: Michael Nickey
'''
stock_symbols = []
num_shares = []
purch_prices = []
current_prices = []
portfolio = {}

def getStocks():
    stocks = input("How many stocks are you entering? ")
    x = 0
    while x < stocks:
        #get input
        stock_symbol = raw_input("\nWhat is the stock symbol? ")
        stock_symbols.append(stock_symbol)
        num_share = raw_input("How many shares? ")
        num_shares.append(num_share)
        purch_price = raw_input("What is the purchase price? ")
        purch_prices.append(purch_price)
        current_price = raw_input("What is the current price? ")
        current_prices.append(current_price)
        x = x + 1
    filter = getFilter() 
    return

def getFilter():
    user_filter = input("\nEnter 1 to sort by stock symbol \
     \nEnter 2 to sort by number of shares \
     \nEnter 3 to sort by purchase price \
     \nEnter 4 to sort by current price.")
    if user_filter == 1:
    #for x in range(len(stock_symbols)):
            #Need to pack the values into a tuple so they can be added as a value.
        print '\nShowing Stock Symbols followed by (Number of Shares, Purchase Price, Current Price)'
        values = zip(num_shares, purch_prices, current_prices)
        portfolio = dict(zip(stock_symbols, values))
        print portfolio
        return 
    elif user_filter == 2:
        print '\nShowing Number of shares followed by (Stock Symbols, Purchase Price, Current Price)'
        values = zip(stock_symbols, purch_prices, current_prices)
        portfolio = dict(zip(num_shares, values))
        print portfolio
        return
    elif user_filter == 3:
        print '\nShowing Purchase Price followed by (Stock Symbols, Number of Shares, Current Price)'
        values = zip(stock_symbols, num_shares, current_prices)
        portfolio = dict(zip(purch_prices, values))
        print portfolio
        return
    else:
        print '\nShowing Current prices followed by (Stock Symbols, Number of Shares, Purchase Price)'
        values = zip(stock_symbols, num_shares, purch_prices)
        portfolio = dict(zip(current_prices, values))
        print portfolio
        return
    return filter
    
if __name__ == '__main__':
    getStocks()
