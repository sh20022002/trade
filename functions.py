''' all none class functions'''
def summery(strategy):
    '''should have to get a formated string with strategy in a logic operatins
    
    short\long-none\sma\50\100\200-none\pricer-none\price-prediction'''
    try:
        term, res, limit, rid, prediction = strategy.split('-')
    except:
        return 'format: short-sma50-200-100-negative'
    return term + res