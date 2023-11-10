
#Exercise 4: Deli

# making a list called sandwich_orders with the names of various sandwiches
sandwichs_orders = ['tuna', 'chicken spicy ranch', 'beef', 'deli(turkey, beef bacon)']

# Now we will make an empty list called finished_sandwiches
finished_sandwiches = []

# Looping through the list of sandwich orders
while sandwichs_orders:
    # taking the first order from the list
    current_order = sandwichs_orders.pop(0)

    # then printing a message for each of the ordered sandwich
    print(f"I made your {current_order} sandwich.")

    #moving the made sandwich to the list of the sandwiches finished
    finished_sandwiches.append(current_order)

# now finally printing a message listing each sandwich which was made and served
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())
