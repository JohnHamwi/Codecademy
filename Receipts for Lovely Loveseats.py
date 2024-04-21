# Descriptions and prices of the furniture items.
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Sales tax rate.
sales_tax = 0.088

# Initializes the customer's total cost and itemization string.
customer_one_total = 0
customer_one_itemization = ""

# Adds the price of the Lovely Loveseat to the total cost and its description to the itemization.
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Adds the price of the Luxurious Lamp to the total cost and its description to the itemization.
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Calculates tax based on the subtotal; however, the calculation is incorrect—it should multiply by the tax rate.
customer_one_tax = customer_one_total + sales_tax

# Adds the incorrectly calculated tax to the total cost.
customer_one_total += customer_one_tax

# Outputs the items purchased and the total cost.
print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total) 
