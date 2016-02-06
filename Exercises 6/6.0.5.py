__author__ = 'Jorian'

def addInterest(balances, rate):
    #newBalance = balance * (1+rate)
    #return newBalance
    for i in range(len(balances)):
        balances[i] = balances[i] * (1+rate)
    return balances

def test():
    amounts = [1000, 2000, 143, 2141, 2455]
    rate = 0.05
    #de amount vernieuw je door de functie addInterest aan te roepen met de waarden 1000 en 0.05. Deze functie
    #returned vervolgens newBalance, die het resultaat in zich huist. Amount is vervolgens newBalance, dus 1050.
    amount = addInterest(amounts,rate)
    print(amounts)

test()