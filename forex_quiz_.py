print("Hello and welcome to my first mini project in Python")

playing=input("Do you want to play a little forex quiz? ")

if playing.lower() !="yes":
    print("Sorry to hear that :( Good Bye then!")
    quit()

print("Oh happy to hear that! Let's play then! Bellow you will find questions related to forex trading :) ")
score=0

answer=input("What means FX in forex? ")
if answer.lower() =="foreign exchange":
    print("You are right!")
    score += 1
else:
    print("You are wrong, correct answer is foreign exchange.")

answer=input("What does ECN stand for when looking at forex brokers? ")
if answer.lower() =="electronic communication network":
    print("You are right!")
    score += 1
else:
    print("You are wrong, correct answer is: electronic communication network ")

answer=input("Let's talk about indexes.. What does CPI stands for? ")
if answer.lower() =="consumer price index":
    print("You are right!")
    score += 1
else:
    print("You are wrong, correct answer is: consumer price index ")

answer=input("What is RSI? ")
if answer.lower() =="relative strength index":
    print("You are right!")
    score += 1
else:
    print("You are wrong, correct answer is: relative strength index")

answer=input("What is NFP? ")
if answer.lower() =="non farm payrolls":
    print("You are right!")
    score += 1
else:
    print("You are wrong, correct answer is: non farm payrolls ")

if score >= 2:
    print("You got " +str(score) + " questions correct!")
    print("You got " +str((score/5)* 100) + "%.")
else:
    print("You got only " +str(score) + " questions correct! Better luck next time!")
    print("You got " +str((score/5)* 100) + "%.")

