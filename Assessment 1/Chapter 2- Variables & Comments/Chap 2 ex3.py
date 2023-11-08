#Exercise 3: Stripping Names,Tidy up the code to make it easier to understandUse a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.Print the name once, so the whitespace around the name is displayed.Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

#creater the name withe whitespaces 
name="\t \n Mohsin \t \n "
#print for whitespaces
print("name with some whitespaces: ")
print(name)
#print for lstrip
print("name with lstrip: ")
print(name.lstrip())
#print for sstrip
print("name with strip: ")
print(name.strip())
#print for rstrip
print("name with rstrip: ")
print(name.rstrip())
