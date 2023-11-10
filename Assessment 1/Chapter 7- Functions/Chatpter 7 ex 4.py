
# Exercise 4: Large Shirts


# Modifing make_shirt function with default values
def make_shirt(size='large', message='I love Python'):
    
    print(f"Made a shirt of size {size.upper()} with the message: '{message}'.")

# Calling the function to make a large shirt with the default message
make_shirt()

# Calling the function to make a medium shirt with the default message
make_shirt(size='medium')

# Calling the function to make a shirt of any size with a different message
make_shirt(size='small', message='Keep Coding!')
