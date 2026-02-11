# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for item in products:
    price_float = float(products[item][0])
    quantity = int(products[item][1])
    total_sales_list.append(price_float * quantity)
    sales = price_float * quantity
    #print(total_sales_list)
    print(f"Total sales for {products[item]} {sales}")
    #print(sum(total_sales_list))
    total_sum = sum(total_sales_list)
    #print(total_sum)
    min_sales = min(total_sales_list)
    max_sales = max(total_sales_list)
    #print(min_sales, max_sales)
    #print("Total sales for: ", products[item])
    
    
    


    