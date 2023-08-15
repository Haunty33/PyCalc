# Asks user for  name and greets them back
# print('Hiyo, What is your name?')
# name = input()
# print('Hiyo, ',name)

#  ** = exponent
#  // = doesn't care about remainder so no 3.5 it would then be 3 ->  integer division
#  % = Modular operator
# if condition operator value or variable
op1 = '-'
op2 = '+'
op3 = '/'
op4 = '*'
operators = op1,op2,op3,op4

print('Type a number: ')
num1 = input()

print('Type an operator example " - + * / " ')
operator = input()

print('Type Another Number: ')
num2= input()

if operator == "*":
    result = int(num1) * int(num2)
    print(result)

elif operator == "-":
    result = int(num1) - int(num2)
    print(result)

elif operator == "+":
    result = int(num1) + int(num2)
    print(result)

elif operator == "/":
    result = int(num1) // int(num2)
    print(result)

else:
    if operator != operators:
        print("Please type a valid operator")
    elif num1 and num2 != int:
        print("Please use one number only")
    else:
        print("Unknown error")