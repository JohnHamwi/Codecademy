# List of available hairstyles and their corresponding prices
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# List of the number of each haircut performed last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Initialize a variable to keep track of the total price of all haircuts
total_price = 0

# Calculate the total price by iterating through the 'prices' list
for price in prices:
    total_price += price

# Calculate the average haircut price
average_price = total_price / len(prices)
print(f"Average Haircut Price: ${average_price}")

# Create a new list with reduced prices (subtracting 5 from each price)
new_prices = [price - 5 for price in prices]
print(f"New Haircut Prices: {new_prices}")

# Initialize a variable to keep track of the total revenue generated
total_revenue = 0

# Calculate the total revenue by multiplying each price by the corresponding number of haircuts last week
for i in range(0, len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print(f"Total Revenue: ${total_revenue}")

# Calculate the average daily revenue
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: ${average_daily_revenue}")

# Create a list of hairstyles with prices under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(f"Haircuts Under $30: {cuts_under_30}")
