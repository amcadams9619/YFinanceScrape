from lxml import html
import requests
import pandas as pd

def findTDValue(searchTree,tdRelatedText):
    tdValue = searchTree.xpath('//td[contains(text(), "'+tdRelatedText+'")]/following-sibling::td[1]/text()')
    if tdValue:
	    return [tdValue[0]] #return first result as list item
    else:
	    return ["N/A"]

def view_data(stock1,stock2) :
#    df = pd.DataFrame({"A":stock2.get_prices(), "B":stock1.get_prices()})
#    return df
    keyStatistics = [
	"Forward P/E",
        "PEG Ratio",
        "Price/Sales",
        "Profit Margin (ttm)",
        "Qtrly Revenue Growth (yoy)",
        "Short % of Float",
        "Beta"
    ]
    symbols = [stock1,stock2]
    resultTable = [["symbol"]+keyStatistics] #append ticker as first column of results

    for symbol3 in symbols: #iterate through tickers
        page = requests.get('http://finance.yahoo.com/q/ks?s='+symbol3+'+Key+Statistics') #pull page data
        tree = html.fromstring(page.text) #parse
        resultRow = [symbol3] #start new result row with first item as the ticker symbol
        for keyStatistic in keyStatistics: #iterate through remaining statistic items, and append to row
            resultRow += findTDValue(tree, keyStatistic)
        resultTable += [resultRow] #write entire row as new record in table
#    fundlist = []
#    for i in resultRow:
#        fundlist.append(float(i))
    print (pd.DataFrame(resultRow, resultTable)) #print result
#    print(fundlist)
