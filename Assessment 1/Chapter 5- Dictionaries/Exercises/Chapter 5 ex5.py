
#Exercise5: Pets
# Creating dictionaries for different pets and their owners
pet_no_1 = {'kind': 'cat', 'owner': 'Shahab'}
pet_no_2 = {'kind': 'cow', 'owner': 'Tayyab'}
pet_no_3 = {'kind': 'parrot', 'owner': 'Asad'}
pet_no_4 = {'kind': 'fish', 'owner': 'Hamdan'}

# Storing the dictionaries in a list called pets
pets = [pet_no_1, pet_no_2, pet_no_3, pet_no_4]

# Looping through the list and then printing information about each ofthe pet revealing its kind and their owners
for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print(f"The {kind} belongs to {owner}.")
