
# Online Python - IDE, Editor, Compiler, Interpreter

while(True):
    try:
        N = int(input("Enter number to check if it's even"))
        break
    except ValueError:
        print("not a valid number")

if (N == 0):
    print("Zero is neither positive or negative")
else:
    if (N % 2 == 0):
        print ("Your number is even!")
    else:
        print("Your number is odd...")



# def sum(a, b):
#     return (a + b)

# a = int(input('Enter 1st number: '))
# b = int(input('Enter 2nd number: '))

# print(f'Sum of {a} and {b} is {sum(a, b)}')
