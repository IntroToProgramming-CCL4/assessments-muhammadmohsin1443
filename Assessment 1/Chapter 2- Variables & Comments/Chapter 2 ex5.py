#Exercise 5: USB Shopper, A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left. You will to use the arithmetic operators to complete this exercise.

# USBs she can get for £50. They are £6 each.
budget=50
price=6
#Calculating how many USBs she can buy
no_of_USBs= budget//price
#Clcukating the amount of money left
money_left= budget%price

#Printing The results
print("She can buy", no_of_USBs, "USB sticks")
print("she will be having", money_left, "Pounds left")
