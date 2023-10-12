toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print("We Sell", num_pizzas, "different kinds of pizza!")

# Create a two-dimensional list called pizza_and_prices
pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

# Sort pizza_and_prices by price in ascending order
pizza_and_prices.sort()

# Get the cheapest pizza (first item in the sorted list)
cheapest_pizza = pizza_and_prices[0]
print("Cheapest pizza:", cheapest_pizza)

# Get the priciest pizza (last item in the sorted list)
priciest_pizza = pizza_and_prices[-1]
print("Priciest pizza:", priciest_pizza)

# Add the new "peppers" pizza topping to the list while keeping it sorted
new_topping = [2.5, "peppers"]
pizza_and_prices.append(new_topping)

# Slice the pizza_and_prices list to get the 3 lowest cost pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
