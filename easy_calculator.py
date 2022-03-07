#first thing we need to do is to define a functions

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

#after defining functions we need to welcome our user and ask him what he would like to do 

print("Hello and welcome to my simple calculator.")
print("-----------------------------------------")
print("Select operation you wish to do.")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

#now we are creating a loop using while. We need an input for user to select an option given above. And then we need to define what those options will do

while True:
    choice=input("Enter your choice(1/2/3/4): ")

    if choice in ('1','2','3','4'):
        number1=float(input("Enter first number: "))     
        number2=float(input("Enter second number: "))
        
        if choice=='1':
            print(number1, "+", number2, "=", add(number1, number2))

        elif choice=='2':
            print(number1, "-", number2, "=", add(number1, number2))

        elif choice=='3':
            print(number1, "*", number2, "=", add(number1, number2))

        elif choice=='4':
            print(number1, "/", number2, "=", add(number1, number2))

        another_calculation=input("Do you wish to do another calculation? (yes/no): ")
        if another_calculation=="no":
            break
    else:
            print("Invalid input")
