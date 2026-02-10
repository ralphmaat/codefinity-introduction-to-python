# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item in inventory:
    current_stock = inventory[item][0]
    minimum_stock = inventory[item][1]
    restock_quant = inventory[item][2]
    sale_status = inventory[item][3]
    print(current_stock)
    print(minimum_stock)
    print(restock_quant)
    print(sale_status)          



    
    
    