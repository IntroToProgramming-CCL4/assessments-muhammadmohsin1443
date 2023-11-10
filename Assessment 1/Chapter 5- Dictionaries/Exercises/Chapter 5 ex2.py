
#Exercise 2: Glossary 
# Writing a glossary dictionary with programming words and their meanings
glossary = {
    'variable': 'A named storage location in memory that holds a value.',
    'function': 'A reusable block of code that performs a specific task.',
    'list': 'An ordered collection of items that can contain elements of different types..',
    'Conditional_statement': "A control structure that allows a program to make decisions based on specified conditions.",
    'loop': 'A control structure which repeatedly executes a specific set of statements while a condition is true.'
}

# Printing each word and its meaning with a newline between each of the pairs
for word, meaning in glossary.items():
    # Print the word followed by a colon and then its meaning
    print(f"{word}:\n{meaning}\n")
