from stockscraper import Company
import time
import os

#TWITTER (TWTR) hasn't had data updated since 10/22 and prices come through as a null which shows up as a none in the JSON
# object breaking the float function. 

Google = 'googl'
Telsa = 'tsla'
Facebook = 'meta' 
Microsoft = 'msft'
Twitter = 'twtr'

if __name__ == '__main__':
    for i in range(5):
        apple = Company('aapl')
        tesla = Company('tsla')
        twitter = Company('twtr')
        Company.show_prices()
        time.sleep(3)
        Company.clean_prices()
        #os.system('cls')
     
