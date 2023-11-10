
#Exercise 3: Glossary 2
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
    
# now we add five more Python terms to our glossary.    
glossary['String'] = 'A sequence of characters enclosed in single or double quotes, used to represent text in Python.'
glossary['Function'] = 'A reusable block of code that performs a specific task.we can define our functions or use built-in functions in Python.'
glossary['Input'] = 'In Python, you can use the input function to receive user input from the keyboard.'
glossary['Print'] = 'This statement is used to display output to the console.'
glossary['Operator'] = 'They are the symbols or keywords in python that are used to perform operations on variables and values.'

# Printing all words and their meanings 
print("\n\n")
for key, value in glossary.items():
    print(key+":","\n"+value+"\n")

