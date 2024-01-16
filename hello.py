# Ask user for their name
# Use the 'input' fuction to read the user name
# Assign the funtion result to a variable 'name'
# A space at end of the string will add a whitespace
# name = input("What's your name? ")

# Remove whitesapce from string and capitalize
# name = name.strip().title()

# Capitalizes the  very first letter
# name = name.capitalize()

name = input("What's your name? ").strip().title()

# Say hello to user
# print the user name using 'print' function
# pass the variable as parameters
# '+' use to pass single parameters
# or '/' use to pass multiple parameters
# end = " " and sep = " " named parameters
# print("hello, end="")
# print(name)
# print("hello, end="???")
# print(name)
# print("hello, sep="???")
# print(name)
# Using "" inside ""
# print("hello,\"Ranga\"")
# print ("hello," + name)
# print ("hello,",name)
print (f"hello, {name}")

first_name, last_name = name.split(" ")
print (f"hello, {first_name}")
print (f"hello, {last_name}")
