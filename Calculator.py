##Python Program to do Arithematic operations with 2 numbers
# Defining Functions for Arithematic operations
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y

# Juust Print Lines for users to See the options 

n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))

print("1 to add")
print("2 to subtract")
print("3 to multiply")
print("4 to divide")

#Choice Variable to Store User Choice
choice = int(input("enter a choice from 1/2/3/4: "))
 
#looping inside for users to do Simple Calculations 
#only exits when Choice is 0
while choice != 0:
    if choice == 1:
        print(add(n1,n2))
    elif choice == 2:
        print(sub(n1,n2))
    elif choice == 3:
        print(mul(n1,n2))
    elif choice == 4:
        print(div(n1,n2))
    else:
	    print("enter the Correct Choice")
    choice = int(input("enter a choice from 1/2/3/4 or 0 to exit: "))
    