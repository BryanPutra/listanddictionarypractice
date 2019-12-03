prices = {'banana': 4, 'apple': 2, 'orange': 1.5, 'pear': 3}
stock = {'banana': 2, 'apple': 0, 'orange': 5, 'pear': 4}
for items in prices:
    print(items)
    print("Prices:", prices[items])
    print("Stock:", stock[items])

total = 0
for items in prices:
    prices[items] * stock[items]
    total = total + prices[items] * stock[items]
print(total)