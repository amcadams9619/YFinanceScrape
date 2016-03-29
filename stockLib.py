import urllib.request as urllib # library that handles linked downloadable files on the web.
import pandas as pd
import statsmodels.formula.api as sm

class Stock : 

    def __init__(self, symbol, open_close) :
        self.symbol = symbol
        self.open_close = open_close

        url = "http://real-chart.finance.yahoo.com/table.csv?s="+symbol+"&d=10&e=11&f=2015&g=d&a=0&b=2&c=1970&ignore=.csv"
        data = urllib.urlopen(url)

        self.open_price = []
        self.close_price = []
        for line in data :
            line = str(line)
            line = line.replace("b'","")
            line = line.replace("\\n","")
            line = line.split(",")

            if (self.open_close == "o") and (line[1] != "Open") :
                self.open_price.append(float(line[1]))
            elif (self.open_close == "c") and (line[4] != "Close") :
                self.close_price.append(float(line[4]))

    def get_prices(self) :
        
        if (self.open_close == "o") :
            return self.open_price
        elif (self.open_close == "c") :
            return self.close_price
       

def reg_summary(stock1,stock2) :
    df = pd.DataFrame({"A":stock2.get_prices(), "B":stock1.get_prices()}) 
    result = sm.ols(formula="A~B", data = df).fit()
    return result.summary()



    
