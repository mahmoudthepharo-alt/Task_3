def calculate_bill(prices, items_bought):
    total = 0
    
    for item in items_bought:
        if item in prices:
            total += prices[item]
    
    return total


prices = {"apple": 0.5, "banana": 0.3}
items_bought = ["apple", "banana"]

print(calculate_bill(prices, items_bought))