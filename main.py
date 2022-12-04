# 1 create toppbings list
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]

# 2 create Pizza list
prices = [2,6,1,3,2,7,2]

# 3 count the number of $2 slices
num_two_dollar_slices = prices.count(2)

# 4 get length
num_pizzas = len(toppings)
print(num_pizzas)

# 5 Print string
stringOut = f"We sell {num_pizzas} different kinds of pizza!"
print(stringOut+"\n")

# 6 Create 2 dim list
pizza_and_prices = [[i,k] for i,k in zip(prices, toppings)]

# 7 Print 2 dim list
print(pizza_and_prices)
print("\n")
# 8  sort increasing price
pizza_and_prices.sort()

# 9 Store first element
cheapest_pizza = pizza_and_prices[:1][:1]

# 10 get most expensive pizza
priciest_pizza = pizza_and_prices[-1:][-1:]

# 11 remove last element 
pizza_and_prices.pop()

# 12 add element at index 5
pizza_and_prices.insert(4,[2.5, "peppers"])

# 13 store the 3 cheapest
three_cheapest = pizza_and_prices[:3][:]

# 14 print the 3 cheapest pizzas
print(three_cheapest)




