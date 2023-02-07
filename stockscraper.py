

#https://api.iex.cloud/v1/data/core/quote/aapl?token=pk_d173656ae7114899a26c660a5ee945f5

#https://cloud.iexapis.com/stable/stock/twtr/quote?token=pk_d173656ae7114899a26c660a5ee945f5

#a piece of data to initiazle some objects
import requests
from prettytable import PrettyTable
api_key = 'pk_d173656ae7114899a26c660a5ee945f5'
class Company:
    prices = []
    BASE_URL = 'https://cloud.iexapis.com/stable/stock'
    def __init__(self, ticker):
        self.ticker = ticker

        self.add_prices_to_list()
    
    @property
    def complete_url(self):
        '''read only attribute to generate the api url'''
        return f'{Company.BASE_URL}/{self.ticker}/quote?token={api_key}'

    @property
    def price(self):
        '''read only attribute to call the quote api and store the price'''
        req = requests.get(self.complete_url).json() #This method will convert the JSON data to a python dict
        try:
            return float(req['iexRealtimePrice'])
        except:
            if req['iexRealtimePrice'] is None:
                return 0
            else:
                print('Error: Non-numeric data type found while returning price.')

    def add_prices_to_list(self):
        Company.prices.append([self.ticker, self.price])
    
    @staticmethod
    def prices_table():
        '''use a static method instead of an instance method'''
        
        pt = PrettyTable(["Ticker Symbol", "Prices"])
        pt.add_rows(Company.prices)
        return pt
    
    @staticmethod
    def show_prices():
        print(Company.prices_table())

    @staticmethod
    def clean_prices():
        Company.prices.clear()