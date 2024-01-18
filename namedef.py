def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

# passing 'to' parameter
# funtion to sound like a verb, 
# saying hello to the user ...
def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)

# defining main function 
# allows to organaize and order the functions in
# any way you want    
def main():
    hello()
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

# squaring a number using def
def main():
    x = int(input("what's x? "))
    print("x square is", square(x))

def square(n):
    n = n*n
    return n

main()

main()