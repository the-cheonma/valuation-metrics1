import yfinance as yf
import pandas as pd
import requests
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt

def s():
    ticker = input("Enter the ticker symbol: ")

    tikr = yf.Ticker(ticker)

    a = si.get_stats_valuation(ticker)
    df1 = pd.DataFrame(a)

    EVbyEBITDA = float((df1.iloc[8,1]))

    b = pd.read_html('https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html')[0]

    df2 = pd.DataFrame(b)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    print("Fetching Sector Wise Data.....")

    print(df2.iloc[2:96, 0:1])

    y = int(input("Choose sector of the company (2-95): "))
    
    
    indavg = float(df2.iloc[y, 3])


    print("{} has an EV/EBITDA of {} , the Industry Average is {}".format(ticker.upper(), EVbyEBITDA, indavg))


    PE = float((df1.iloc[2,1]))

    c = pd.read_html('https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/pedata.html')[0]
    df3 = pd.DataFrame(c)
    
    z = y-1                        
    PEindavg = float(df3.iloc[z ,3])

    print("{} has a Trailing P/E of {}, the Industry Average is {}".format(ticker.upper(), PE, PEindavg))

    #url = "https://www.marketwatch.com/investing/stock/{}/financials/cash-flow"
    #url1 = url.format(ticker)

    #df4 = pd.read_html(url1)[6]

    #print(df4.iloc[22, 5])

    #mcap = df1.iloc[0, 1]
    #mcap1 = mcap.replace('B', '')

    #print(mcap1)

    #FCFY

    plt.bar(-0.2, EVbyEBITDA, width=0.04, color='b', align='center')
    plt.bar(+0.2, indavg, width=0.04, color='r', align='center')
    plt.title("{}'s EV/EBITDA vs. Industry Average".format(ticker.upper()))
    plt.ylabel("EV/EBITDA")
    plt.xticks([])
    plt.legend(["{}'s EV/EBITDA".format(ticker.upper()), "Industry Average"])
    plt.show()

    plt.bar(-0.2, PE, width=0.04, color='b', align='center')
    plt.bar(+0.2, PEindavg, width=0.04, color='r', align='center')
    plt.title("{}'s P/E vs. Industry Average".format(ticker.upper()))
    plt.ylabel("P/E Ratio")
    plt.xticks([])
    plt.legend(["{}'s P/E".format(ticker.upper()), "Industry Average"])
    plt.show()
    y_n()
def y_n ():
    j = input("Check Another Stock(Y/n)?:")
    if j.upper() == 'Y':
        print("------------------------------------")
        s()
    elif j.upper() == 'N':
        exit()
    else:
        print("Invalid Input, Try Again!")
        y_n()

s()
