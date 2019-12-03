groceries = ["banana","orange","apple"]
stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
#def compute_bill(food):
    #total = 0
    #for items in food:
        #total = total + prices[items]   #<<<FOR PRACTICE FIRST PART OF NUMBER
    #return total
#print(compute_bill(prices))

def compute_bill(food):
    total = 0
    for items in food:
        if stock[items] > 0:
            total = total + prices[items]
            stock[items] = stock[items] - 1
    return total
print(compute_bill(groceries))
print(stock)