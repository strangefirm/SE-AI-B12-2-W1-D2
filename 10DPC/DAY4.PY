print("For loop example ")
print("Multiplication table ")
n = int(input("Enter the number of table: "))
for i in range(1, 11):
    print(i, "x", n, "=", i * n)
    
print("*******************************")
print("Passing a dictionary to a for loop example ")
print("*******************************")
#shopping cart example
cart = {
    "Laptop": 75000,
    "Mouse": 800,
    "Keyboard": 1500
}

total = 0

for product, price in cart.items():
    print(product, ":", price)
    total += price
print("Total amount: ₹", total) 
print("*******************************")
print("Creating a dictionary from two lists example ")
print("*******************************")

products = ["Laptop", "Mouse", "Keyboard"]  #list1
prices = [75000, 800, 1500]                 #list2

product_prices = {}                         #dict name
totalnew=0

for i in range(len(products)):
    product_prices[products[i]] = prices[i]
print(product_prices)
for product, price in product_prices.items():
    print(product, "costs ₹", price)
    totalnew += price
print("Total amount: ₹", totalnew) 