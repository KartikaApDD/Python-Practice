import random

QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
GOOD_COMMENTS = ["Great!", "Amazing!", "Fantastic!"]
BAD_COMMENTS = ["Trying better!", "You can do that!", "Don't give up, just try!"] 
QUESTIONS = ["Do you know what my favourite food is?"]
OPTIONS = [["Chicken", "Rice", "Cake", "Sushi"]]
SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [3]

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
    score = 0
    
    #loop each question/answer
    for i in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
            # Ask the user a question
            answer = input (QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                                OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
            
            # Check the user's answer and give feedback
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                print("Yey, you got it right!")
                score+= 20
                print(random.choice(GOOD_COMMENTS))
                break
            elif answer == "":
                print("Oh, you didn't answer anything")
            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("Wrong!")
                print(random.choice(BAD_COMMENTS))
            else:
                print("Ops! That's not the option")


            question_attempts -= 1
        print("The answer is sushi")
    
    # End the quiz
    print("Well done {}! You have finished your quiz, you got, {}, points. Let's play again later!".format(name,score))
    
    # Replay
    play = input ("Do you still want to play?").lower()

print("Goodbye")