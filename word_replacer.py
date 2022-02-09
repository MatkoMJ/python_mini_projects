sentence=input("Enter your sentence here: ")
print("Your sentence is: " + sentence)

question=input("Did you typed your question right? ")

if question.lower() !="no":
    print("Okay nice to hear that! Have a good day! And see you when you make a mistake in typing haha :) ")
    quit()
else:
    print("Okay lets replace a word in your sentence")
    word1=input("Enter the word to replace: ")
    word2=input("Enter the word to replace with: ")
    print("You new sentence is: " + sentence.replace(word1,word2))
