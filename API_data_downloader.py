import yfinance as yf
import json
from time import sleep
from multiprocessing import Process
from pymongo import MongoClient
import pprint

def get_tickers():
	stocks=input("Please Enter the number of stocks you want to Track: ")
	ticker_list=[]
	for i in range(int(stocks)):
		ticker_list.append(input("Please enter the ticker for stock {}: ".format(i+1)))
	return ticker_list

def drop_collection():
	stock_data=dict()
	client = MongoClient()
	db=client.test
	stocks=db.stocks
	stocks.drop()


def consume_data_from_api(*tickers):
	stock_data=dict()
	client = MongoClient()
	db=client.test
	stocks=db.stocks
	while True:
		for ticker in tickers:
			stocks.delete_one({'ticker': ticker})
			stock_data['ticker']=ticker
			stock_data['data']=yf.Ticker(ticker).info
			stocks.insert_one(stock_data)
			stock_data.clear()
		sleep(30)

def view_stocks(tickers):
	pp = pprint.PrettyPrinter(indent=4)
	client = MongoClient()
	db=client.test
	stocks=db.stocks
	interface=True
	while interface:
		print("\n\nTo view all stocks in database enter 1")
		print("To view stocks by ticker enter 2")
		print("To exit program enter 3")
		x=input("Your input: ")
		if x=='1':
			result=stocks.find()
			for item in result:
				pp.pprint(item)
				print('\n===========\n')
		elif x=='2':
			y=input("Please specify the ticker: ")
			if not y in tickers:
				print('Ticker not found in database: ')
				continue
			result=stocks.find_one({'ticker': y})
			pp.pprint(result)
		elif x=='3':
			interface=False



def main():
	drop_collection()
	ticker_list=get_tickers()
	p=Process(target=consume_data_from_api, args=(ticker_list))
	p.start()
	view_stocks(ticker_list)
	p.terminate()
	p.join()



if __name__=="__main__":
	main()

