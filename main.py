import random
GOOD_COMMENTS = ["Great!", "Amazing!", "Fantastic!"]
BAD_COMMENTS = ["Trying better!", "You can do that!", "Don't give up, just try!"] 
score = 0
play = "yes"

# Ask the user their name and save it 
name = input("What's your name?")

# Greet the user and introduce the quiz 
print("Welcome to the quiz,", name)
print("I hope you have a nice day today!")
print("In this quiz you need to guess what my favourite food is")

# check number of qestion attempts
while True:
    try:
        tries = input("How many attempts do you want at each question? 1-4")
        tries = int(tries)
        break  
    except:
        print("That's not a number")

# Repeat quiz
while play == "yes":

    question_attempts = tries
    while question_attempts > 0:
    # Ask the user a question
        question = "Do you know what my favourite food is?"
        a = "Chicken"
        b = "Rice"
        c = "Cake"
        d = "Sushi"
        answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d)).lower()

        # Check the user's answer and give feedback
        if answer == d.lower() or answer == "d":
            print("Yey, you got it right!")
            score+= 20
            print(random.choice(GOOD_COMMENTS))
            break
        elif answer == "":
            print("Oh, you didn't answer anything")
        elif answer != c.lower() and answer != "c" and answer != a.lower() and answer != "a" and answer != b.lower() and answer != "b":
            print("Ops! That's not the option")
        else:
            print("Wrong!")
            print(random.choice(BAD_COMMENTS))

            question_attempts -= 1
            print("Quite right but the correct answer is Sushi!")
    
    # End the quiz
    print("Well done {}! You have finished your quiz, you got, {}, points. Let's play again later!".format(name,score))
    
    # Replay
    play = input ("Do you still want to play?").lower()

print("Goodbye")