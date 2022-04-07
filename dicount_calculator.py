#simple discount calculator
#so we need inputs,and if statements...

amount=int(input("Enter amount: "))  #asking user to input a number 
if amount<1000:
    discount=amount*0.05  #you can change this number ofc. So if number is less than 1k user gets 0.5% discount
    print ("Discount",discount)
else:
    discount=amount*0.10 #also you can change this one... so if number is more than 1k user gets 0.10% discount
    print ("Discount",discount)

print ("Net payable:",amount-discount)  #at the end we need to print out and show user what he needs to pay after the discount. Enjoy :)
