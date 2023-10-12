# Ground Shipping

# Weight of the package
weight = 10

# Flat charge for ground shipping
flat_charge = 20.00

# Calculate the cost of ground shipping
if weight <= 2:
    ground_price_per_pound = 1.50
elif weight <= 6:
    ground_price_per_pound = 3.00
elif weight <= 10:
    ground_price_per_pound = 4.00
else:
    ground_price_per_pound = 4.75

# Calculate the total cost
ground_shipping_cost = ground_price_per_pound * weight + flat_charge

# Print the cost of shipping
print("The cost of ground shipping a package weighing", weight, "pounds is $", ground_shipping_cost)

# Cost of premium ground shipping
premium_shipping_cost = 125.00  # You can adjust the cost as needed

# Print the cost of premium ground shipping
print("The cost of premium ground shipping is $", premium_shipping_cost)

# Drone Shipping

if weight <= 2:
    drone_price_per_pound = 4.50
elif weight <= 6:
    drone_price_per_pound = 9.00
elif weight <= 10:
    drone_price_per_pound = 12.00
else:
    drone_price_per_pound = 14.25

# Calculate the total cost
drone_shipping_cost = drone_price_per_pound * weight

# Print the cost of shipping
print("The cost of drone shipping a package weighing", weight, "pounds is $", drone_shipping_cost)