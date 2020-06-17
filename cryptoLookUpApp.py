import json
from requests import Session,Request
from decouple import config
from tkinter import *
import os
os.system('cls')

def color(amt):
    if amt >= 0:
        return 'green'
    else:
        return 'red'


root = Tk()

root.title('Crypto Currency App')



#*******************************GUI HEADER*************************************************************************
header_name = Label(root, text='Name', bg='white', font = 'Helvetica 8 bold')
header_name.grid(row=0, column=0, sticky=N+S+E+W)

header_rank = Label(root, text='Rank', bg='silver', font = 'Helvetica 8 bold')
header_rank.grid(row=0, column=1, sticky=N+S+E+W)

header_current_price = Label(root, text='Current Price', bg='white', font = 'Helvetica 8 bold')
header_current_price.grid(row=0, column=2, sticky=N+S+E+W)

header_price_paid = Label(root, text='Price Paid', bg='silver', font = 'Helvetica 8 bold')
header_price_paid.grid(row=0, column=3, sticky=N+S+E+W)

header_profit_loss_per = Label(root, text='Profit/Loss Per', bg='white', font = 'Helvetica 8 bold')
header_profit_loss_per.grid(row=0, column=4, sticky=N+S+E+W)

header_1_hr_change = Label(root, text='1 HR Change', bg='silver', font = 'Helvetica 8 bold')
header_1_hr_change.grid(row=0, column=5, sticky=N+S+E+W)

header_24_hr_change = Label(root, text='24 HR Change', bg='white', font = 'Helvetica 8 bold')
header_24_hr_change.grid(row=0, column=6, sticky=N+S+E+W)

header_7_day_change = Label(root, text='7 Day Change', bg='silver', font = 'Helvetica 8 bold')
header_7_day_change.grid(row=0, column=7, sticky=N+S+E+W)

header_current_value = Label(root, text='Current Value', bg='white', font = 'Helvetica 8 bold')
header_current_value.grid(row=0, column=8, sticky=N+S+E+W)

header_profit_loss_total = Label(root, text='Profit/Loss Total', bg='silver', font = 'Helvetica 8 bold')
header_profit_loss_total.grid(row=0, column=9, sticky=N+S+E+W)

#**************************************END GUI HEADER***********************************************************


myBcoinPL = 0
def cryptoApp():

    api_key = config('APICONNECT')

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key,

    }



    session = Session()
    session.headers.update(headers)
    response = session.get(url)
    #print(response.status_code)

    api = json.loads(response.content)


    #bCoin = ['BTC','XRP','EOS','STEEM']
    myBcoin = [
    		{
    			'symbol': 'BTC',
    			'amount_owned': 0,
    			'price_paid_per': 0
    		},

    		{
    			'symbol': 'STEEM',
    			'amount_owned': 3000,
    			'price_paid_per': .80
    		},
    		{
    			'symbol': 'XRP',
    			'amount_owned': 5000,
    			'price_paid_per': .20
    		},
    		{
    			'symbol': 'XLM',
    			'amount_owned': 2000,
    			'price_paid_per': .10
    		},
    		{
    			'symbol': 'EOS',
    			'amount_owned': 1000,
    			'price_paid_per': 2.00
    		}
    	]


    totalCurrentValue = 0
    myBcoinPL = 0
    rowCount = 1
    pile = []

    for x in api['data']:
        for coin in myBcoin:
            if coin['symbol'] == x['symbol']:
                #math calculations

                totalPaid = float(coin['amount_owned']) * float(coin['price_paid_per'])
                currentValue = float(coin['amount_owned']) * float(x['quote']['USD']['price'])
                profitLoss = currentValue - totalPaid
                myBcoinPL += profitLoss
                profitLossPerCoin = float(x['quote']['USD']['price']) - float(coin['price_paid_per'])
                totalCurrentValue += currentValue

                '''
                print(x['name'])
                print('Current Price: ${0:.2f}'.format(float(x['quote']['USD']['price'])))
                print('Profit/Loss Per Coin: ${0:.2f}'.format(float(profitLossPerCoin)))
                print('Rank: ',x['cmc_rank'])
                print('Total Paid: ${0:.2f}'.format(float(totalPaid)))
                print('Current Value: ${0:.2f}'.format(float(currentValue)))
                print('Profit/Loss: ${0:.2f}'.format(float(profitLoss)))


                #print(x['name'])
                #print('${0:.2f}'.format(float(x['quote']['USD']['price'])))
                #print('Rank:', x['cmc_rank'])
                print('--------------------------------------------------------------------------------')

                #print(x['quote']['USD']['price'])

    print('Portfolio P/L:${0:.2f}'.format(float(myBcoinPL)))
                '''


                name = Label(root, text=x["name"], bg="white")
                name.grid(row=rowCount, column=0, sticky=N+S+E+W)

                rank = Label(root, text=x['cmc_rank'], bg='silver')
                rank.grid(row=rowCount, column=1, sticky=N+S+E+W)

                current_price = Label(root, text='${0:.2f}'.format(float(x['quote']['USD']['price'])), bg='white',)
                current_price.grid(row=rowCount, column=2, sticky=N+S+E+W)

                price_paid = Label(root, text='${0:.2f}'.format(float(coin['price_paid_per'])), bg='silver')
                price_paid.grid(row=rowCount, column=3, sticky=N+S+E+W)

                profit_loss_per = Label(root, text='${0:.2f}'.format(float(profitLossPerCoin)), bg='white', fg=color(float(profitLossPerCoin)))
                profit_loss_per.grid(row=rowCount, column=4, sticky=N+S+E+W)

                one_hr_change = Label(root, text='{0:.2f}%'.format(float(x['quote']['USD']['percent_change_1h'])), bg='silver', fg=color(float(x['quote']['USD']['percent_change_1h'])))
                one_hr_change.grid(row=rowCount, column=5, sticky=N+S+E+W)

                tf_hr_change = Label(root, text='{0:.2f}%'.format(float(x['quote']['USD']['percent_change_24h'])), bg='white', fg=color(float(x['quote']['USD']['percent_change_24h'])))
                tf_hr_change.grid(row=rowCount, column=6, sticky=N+S+E+W)

                seven_day_change = Label(root, text='{0:.2f}%'.format(float(x['quote']['USD']['percent_change_7d'])), bg='silver', fg=color(float(x['quote']['USD']['percent_change_7d'])))
                seven_day_change.grid(row=rowCount, column=7, sticky=N+S+E+W)

                current_value = Label(root, text='${0:.2f}'.format(float(currentValue)), bg='white')
                current_value.grid(row=rowCount, column=8, sticky=N+S+E+W)

                profit_loss_total = Label(root, text='${0:.2f}'.format(float(profitLoss)), bg='silver', fg=color(float(profitLoss)))
                profit_loss_total.grid(row=rowCount, column=9, sticky=N+S+E+W)

                rowCount += 1


    portfolio_profits = Label(root, text="P/L: ${0:.2f}".format(float(myBcoinPL)), font="Helvetica 8 bold", fg=color(float(myBcoinPL)))
    portfolio_profits.grid(row=rowCount, column=0, sticky=W, padx=10, pady=10)

    root.title("Crypto Currency App - Portfolio Value: ${0:.2f}".format(float(totalCurrentValue)))

    api = ''
    update_button = Button(root, text="Update Prices", command=cryptoApp)
    update_button.grid(row=rowCount, column=9, sticky=E+S, padx=10, pady=10)


cryptoApp()

root.mainloop()
