
prices = {"Apple": 1000, "Banana": 500, "Mango": 1200}


for fruit, price in prices.items():
    print(f"{fruit}: {price} RWF per kg")


total_cost = 0
for price in prices.values():
    total_cost += price * 2 


print(f"Total cost for 2kg of each fruit: {total_cost} RWF")
