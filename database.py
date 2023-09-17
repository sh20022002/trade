'''all database acrions'''
import pymongo



local_host = '' '''url path'''


mycliant = pymongo.MongoClient(local_host)

mydb = mycliant['stocks-consumer']

mycol = mydb['stocks']
mycol2 = mydb['cliant']

'''no need for this method'''
def insert_stock(name, symbol):
    x = '{name' + f':{name},' + 'symbol' + f':{symbol}' + '}'
    data = mycol.insert_one(x)


def insert_stocks(names, symbols):
    data = []
    for name, symbol in zip(names,symbols):
        x = '{name' + f':{name},' + 'symbol' + f':{symbol}' + '}'
        data.insert(x)
    data = mycol.insert_many(x)

def find_s(symbol):
    '''!returns if found'''
    mycol.find_one(symbol)

def find_stock(symbol):
    pass
'''returns al stock data and inits it in a compeny object'''

def remove_from_db(symbol):
    pass