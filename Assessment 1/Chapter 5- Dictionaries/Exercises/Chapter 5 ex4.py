
#Exercise4: Rivers
# Creating a dictionary for the major rivers and the countries in which they run through.
rivers_of_the_world = {'amazon': 'Brazil','yangtze': 'China','nile': 'Egypt','Indus': 'Pakistan'}

#by using a loop to print a sentence about each river
for river, country in rivers_of_the_world.items():
    print(f"The {river.title()} runs through {country}.")

# By using a loop to print the name of each river
print("\nRivers of the world:")
for river in rivers_of_the_world.keys():
    print(river.title())

#by using a loop to print the name of each country
print("\nCountries in which they run through:")
for country in rivers_of_the_world.values():
    print(country)

