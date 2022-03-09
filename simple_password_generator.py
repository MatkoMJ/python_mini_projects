import random

uppercase_letters="ABCDEFGFIJKLMNOPQRSTUVWXYZ"
lowercase_letter=uppercase_letters.lower()
numbers="0123456789"
symbols="(),:*+!$@#"

upper,lower,nums,syms=True, True, True, True  #if you dont want for example numbers to be used just change 3rd True value to False :) 

everything=""
if upper:
    everything+=uppercase_letters
if lower:
    everything+=lowercase_letter
if nums:
    everything+=numbers
if syms:
    everything+=symbols

length=int(input("Input the length of the password: "))
amount=int(input("Input the amount of passowrds you would like to be generated: "))

for x in range(amount):
    password="".join(random.sample(everything, length))
    print("Here is your random passowrd: ")
    print(password)
