score = 0
# Ask the user their name and save it 
name = input("What's your name?")

# Greet the user and introduce the quiz
print("Welcome to the quiz, Gles")
print("I hope you have a nice day today!")
print("In this quiz you need to guess what my favourite food is")

# Ask the user a question
answer = input("Do you know what my favourite food is?")

# Check the user's answer and give feedback
if answer == "sushi":
    print("Yey, you got it right!")
    score+= 20
elif answer == "":
    print("Oh you didn't know that? My favourite food is sushi")
else:
    print("You don't get it right. It's sushi")
    score+= 7
# End the quiz
print("Well done! You have finished your quiz, you got", score, "points")
