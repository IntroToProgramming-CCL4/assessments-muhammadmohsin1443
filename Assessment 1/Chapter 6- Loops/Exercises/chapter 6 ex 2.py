
#Exercise 2: Movie Tickets:
while True:
    # making the user to enter their age
    age_str = input("Dear user, please enter your age (or 'quit' to exit): ")

    # we check if the user wants to quit
    if age_str.lower() == 'quit':
        break

    try:
        # we then convert the input to an integer
        age = int(age_str)

        # Determining the cost of the movie ticket based on age
        if age < 3:
            print("Dear user, your movie ticket is free.")
        elif 3 <= age <= 12:
            print("Dear user, the cost of your movie ticket is $10.")
        else:
            print("Dear user, the cost of your movie ticket is $15.")

    except ValueError:
        print("Dear user, Please enter a valid age (or 'quit' to exit).")

