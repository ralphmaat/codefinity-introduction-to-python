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
    print(f"Processing {item}")
    current_stock = inventory[item][0]
    minimum_stock = inventory[item][1]
    restock_quant = inventory[item][2]
    sale_status = inventory[item][3]
    #print("Item ",item)
    #print("Current stock: ",current_stock)
    #print("Minimum stock: ",minimum_stock)
    #print("Restock quant.: ",restock_quant)
    #print("Sales status: ", sale_status)
    while (current_stock < minimum_stock):
        inventory[item][0] += restock_quant
        current_stock = inventory[item][0]
        print(inventory)
    if current_stock > discount_threshold and not sale_status:
        inventory[item][3] = True
    inventory[item][0] = current_stock
print("Processing completed")

  
        
    

    
    
    