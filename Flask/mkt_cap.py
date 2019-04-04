#Dependencies
import requests
import json
import pandas as pd
from Config import pwd, user, host, port, dbname 


# SQL Alchemy
from sqlalchemy import create_engine,Column, Integer, String, Float, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()

# --------------------------------------------------------------------
# PURPOSE
# --------------------------------------------------------------------
# this script will be used to add market capitalization to stock database..
# using iex api - https://iextrading.com/developer/docs/

# --------------------------------------------------------------------
# ESTABLISH DATABASE CONNECTION USING VIV'S AWESOME CODE :)
# # --------------------------------------------------------------------
# host="stock-data-analysis.ciuxgx1cjbsw.us-east-2.rds.amazonaws.com"

# port=3306

# dbname="stock_data"

# user="ucbx"

password= pwd

conn = pymysql.connect(host, user=user,port=port,

                          passwd=password, db=dbname)
# --------------------------------------------------------------------
# CREATE STOCK TICKER LIST
# --------------------------------------------------------------------

# read stock tickers into dataframe
tickers = pd.read_sql('select symbol\
                          from sandp_stocks;', 
                          con=conn)

# convert tickers df into list that can be used for IEX API call
tickers_list = tickers.values.tolist()

# our tickers_list returns a list of lists ([['MMM'], ['ABT'], ['ABBV']...) 
# so we need to unzip it into just a list of strings [('MMM', 'ABT', 'ABBV'....)
tickers_list = zip(*tickers_list)
tickers_list = list(tickers_list)
tickers_list = tickers_list[0]
print(tickers_list)

# --------------------------------------------------------------------
# IEX API CALL FOR MARKET CAPITALIZATION - https://api.iextrading.com/1.0/stock/aapl/stats
# --------------------------------------------------------------------

url = 'https://api.iextrading.com/1.0/stock/'

# create empty dictionary to hold stock ticker and market caps as key value pairs 
mkt_caps = {}

for tick in tickers_list:
    
    try:
           
    # define target url
            target_url = f"{url}{tick}/stats"
    
    # make api call to iex
            response = requests.get(target_url).json()
            mkt_cap = response['marketcap']
       
    # populate dictionary with ticker as key and market cap as value
            mkt_caps[tick] = {'market_cap_2019':mkt_cap}
            
    # insert 0 as market cap for any ticker with no label    
    except json.decoder.JSONDecodeError:
            mkt_caps[tick] = {'market_cap_2019':0}

# place market cap info into pandas dataframe
mkt_cap_df = pd.DataFrame(mkt_caps).T

# replace 'blank' string with 0
# note - only doing this bc loop originally populated BRK-B with 'blank'
mkt_cap_df.replace('blank', 0,inplace=True)


# rename dataframe index to symbol then reset index to standard integer index
mkt_cap_df = mkt_cap_df.rename_axis('symbol')
mkt_cap_df.reset_index(inplace=True)

# --------------------------------------------------------------------
# PUSH MARKET CAP INFO TO TABLE IN DATABASE 
# --------------------------------------------------------------------

Base = declarative_base()

# connect to local MySQL workbench
eng_link = f"mysql://{user}:{password}@{host}/{dbname}"
engine = create_engine(eng_link)

# establish a connection to the local DB
conn1 = engine.connect()

# declare class for market cap table
class stock_market_cap (Base):
     __tablename__ = 'stock_market_cap'
     symbol = Column(String(10),primary_key=True)
     Market_Cap = Column(Integer)

# create market cap table in database
Base.metadata.create_all(conn1)

# confirming that tables got created in the DB
engine.table_names()

# Create a session that binds engine to enable data entry
session = Session(bind=engine)

# rename market_cap_2019 column name to match name class declaration
mkt_cap_df.rename(columns={'market_cap_2019': 'Market_Cap'}, 
                  inplace=True)

# push market cap table to database
mkt_cap_df.to_sql(name="stock_market_cap", 
                  con=engine, 
                  if_exists='replace',
                  index=False)









