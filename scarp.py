#scrap table using pandas and beautifulsoup + request libs.

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def main():
    
    #show in terminal as tabulate form !
    res = requests.get("http://www.rajkotbusinessguide.com/categories/Precision/251")
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('table')[6] 
    df = pd.read_html(str(table))
    print( tabulate(df[0], headers='keys', tablefmt='psql') )
    
    #convert into json 
    # res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")
    # soup = BeautifulSoup(res.content,'lxml')
    # table = soup.find_all('table')[0] 
    # df = pd.read_html(str(table))
    # print(df[0].to_json(orient='records'))

if __name__ == '__main__':main()
