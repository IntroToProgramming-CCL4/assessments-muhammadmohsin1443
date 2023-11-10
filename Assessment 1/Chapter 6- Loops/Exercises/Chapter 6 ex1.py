
#Exercise 1: Pizza Toppings 
# Initializing an empty list to store pizza toppings data
pizza_toppings = []

# Making the user enter pizza toppings
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").lower()
# Checking if the user wants to quit,so we print a message and break out of the loop
    if topping == 'quit':
        if topping == 'quit':
             print("Okay, your pizza is ready!")
        break  # Exit the loop if the user enters 'quit'
    else:
        pizza_toppings.append(topping)
        print(f"You'll add {topping} to your pizza.")

# Printing the final list of pizza toppings
print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print("- " + topping)
