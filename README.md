# **WallStofTheWest Project Summary**

## Purpose

- **Analyzing year over year % returns of stocks in the S&P 500 from 2009-2018** to understand if there were specific industry sectors and/or stocks that regularly outperformed the yearly overall return of the S&P 500

- **Using data to determine which sectors in the S&P 500 had the highest performance** based on average yearly returns from 2009-2018

- **Develop a set of valuation methods to determine future ROI** based on knowledge of the market

- **Create a protfolio of stocks for investment** based on aforementioned analysis based on a set of pre-determined investment methods

- **Predict the future price of stocks upto 3 months in advance** using Quandl for data, R for analysis, and LS-SVM methods that emply a sliding window to train data sets 

- **Determine if Sentiment Analysis can help fine tune the LS-SVM model** based on Presidential influence through the use of Twitter

### [Heroku deployed website](https://stock-market-analysis.herokuapp.com/)
----

## Architecture
### APIs
- [IEX](https://iextrading.com/developer/docs/#key-stats)
    - Market Capitalization
- [Alphavantage](https://www.alphavantage.co/documentation/)
    - Daily stock price
    - Disbursements (eg Dividends)
- [Tiingo](https://api.tiingo.com/)
    - Confirmation of correct daily stock price data
- [Quandl](https://www.quandl.com/data/EOD-End-of-Day-US-Stock-Prices)
    - Comprehensive stock API

### Web Scraping
 - Wikipedia
 - Marketbeat

### Database
- Amazon Web Services 
    - MySQL instance

### Extract Transform Load 
- Python and Pandas
- R Studio
- MySQL

### Visuals 
- R Studio
- Java Script 
   - Plotly
   - FusionCharts
   - Tableau

### Deployment - Flask & Heroku

