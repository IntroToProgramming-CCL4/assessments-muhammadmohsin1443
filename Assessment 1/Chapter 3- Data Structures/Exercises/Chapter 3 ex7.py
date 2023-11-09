# Exercise 7: Seeing the World 

# Storing the locations in a randomize sequenced list
Famous_Locations =["Islamabad","Abu Dhabi","Riyadh","Madina","Makkah","Doha",] 

# Now we print the list in its original order
print("Original order:", Famous_Locations)

# Printing the list in an alphabetical order without modifying the original list
print("Alphabetical order:", sorted(Famous_Locations))

# Printing the list to just show that it is still in its original order or form 
print("Original order:", Famous_Locations)

# Printing the list in a reverse alphabetical order without doing any changings to the order of the original list
print("Reverse alphabetical order:", sorted(Famous_Locations, reverse=True))

# Printing the list to just show that it is still in its original order or form 
print("Original order:", Famous_Locations)

# Now we change the order of the list using reverse() function
Famous_Locations.reverse()

# Printing the list to show that its order has been changed
print("Changed order:", Famous_Locations)

# Now again canging the order of the list again using reverse()
Famous_Locations.reverse()

# Printing the list just to show that it is back to its original form or order
print("Original order:", Famous_Locations)

#Now we change the order of the list using sort() function
Famous_Locations.sort()

# Printing the list to show that its order has been changed
print("Changed order:", Famous_Locations)

# Changing the order of the list using sort() function in reverse alphabetical order
Famous_Locations.sort(reverse=True)

# Printing the list to just show that its order has been changed
print("Changed order:", Famous_Locations)