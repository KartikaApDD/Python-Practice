score = 0
QUESTION_FORMAT= "{}\nA.{} B.{} C.{} D.{}"
# Ask the user their name and save it 
name = input("What's your name?")

# Greet the user and introduce the quiz
print("Welcome to the quiz, Gles")
print("I hope you have a nice day today!")
print("In this quiz you need to guess what my favourite food is")

# Ask the user a question
question = "Do you know what my favourite food is?"
a = "Chicken"
b = "Rice"
c = "Cake"
d = "Sushi"
answer = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()

# Check the user's answer and give feedback
if answer == d.lower() or answer == "d":
    print("Yey, you got it right!")
    score+= 20
elif answer == "":
    print("Oh, you didn't answer anything")
elif answer != c.lower() and answer != "c" and answer != a.lower() and answer != "a" and asnwer != b.lower() and answer != "b":
    print("Ops! That's not the option")
else:
    print("Sadly, wrong!")
    print("The answer is sushi")
# End the quiz
print("Well done {}! You have finished your quiz, you got, {}, points. Let's play again later!".format(name,score))
