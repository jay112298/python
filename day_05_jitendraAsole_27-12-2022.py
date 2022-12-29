#Make a set using the set() method

x = set()

#Add item to the set using add()

x.add(1)
print(x)
x.add(2)
print(x)
x.add(3)
print(x)

#List with repeated items

int_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(set(int_list))

print(int_list)

#Boolean, set a boolean value to true

bool = True

bool = None

print(bool)

#Operators

a = 3 
b = 4 

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#Number conditionals

print(2 > 4)
print(2 < 4)
print(2 == 4)
print(2 <= 4)
print(2 >= 4)

#If Else

loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the auto shop')
elif loc == 'Bank':
    print('Welcome to the bank')
else:
    print('Where are you?')


# Check if else using 2 numbers

a = 55
b = 6

if a>b :
    print("A is greater than B")
else :
    print("A is less than B")

numA = int(input("Please enter the value of A: "))
numB = int(input("Please enter the value of B: "))


if numA>numB :
    print("A is greater than B")
else :
    print("A is less than B")

#Also check if they are equal

numA = int(input("Please enter the value of A: "))
numB = int(input("Please enter the value of B: "))


if numA>numB :
    print("A is greater than B")
elif numA == numB :
    print("A is equal to B")
else :
    print("A is less than B")

