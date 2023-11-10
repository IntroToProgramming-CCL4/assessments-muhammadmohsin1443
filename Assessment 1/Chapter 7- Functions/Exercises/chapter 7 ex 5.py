
#Exercise 5: Cities

# Defining a function called describe_city with a default country value
def describe_city(city, country='default country'):
    print(f"{city.title()} is in {country.title()}.")

# Calling the function for three different cities
describe_city('islamabad', 'Pakistan')
describe_city('Dubai', 'Uae')
describe_city('Riyadh')  # Using the default country value
