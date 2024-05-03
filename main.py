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
else:
    print("You don't get it right. It's sushi")

# End the quiz
print("Oh no the quiz has ended! Sad to hear it but I am happy that you want to use mine.")
