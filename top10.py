guesses = []
BEST_SELLING_MUSIC_ARTISTS_ANSWERS = ["The beatles", "Michael Jackson", "Elvis Presley", "Elton John", "Queen", "Madonna", "Led Zeppelin", "Rihanna", "Pink Floyd", "Eminem"]

# ------ FUNCTIONS ------

# Welcome user and introduces the quiz
def intro ():
    # Ask the user their name and save it 
    name = input("What's your name?")

    # Greet the user and introduce the quiz 
    print("Welcome to the quiz,", name)
    print("I hope you have a nice day today!")
    print("In this quiz you need to guess what my favourite food is")

def getLives():
    while True: 
        lives = input("How many chances do you want?")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except: 
                print("That wasn't a number")

def inList(answer, list): 
    if answer in list:
        return True
    else:
        return False

# ------ MAIN CODE ------

intro()
lives = getLives()
score = 0

while lives > 0:
    answer = input("Name one of the top best selling music artist all the time:\n").lower()

    if inList(answer, BEST_SELLING_MUSIC_ARTISTS_ANSWERS):
        if inList(answer, guesses):
            print("You've guessed that alreasy")
        else:
            print("Correct")
            score += 5
            guesses.append(answer)
            print("You have guessed {}. Your score is {}. You have {} chances remaining".format(len(guesses), score))
    else:
        print("Wrong")
        score -= 1
        guesses.append(answer)
        print("You have guessed {}. Your score is {}. You have {} chances remaining".format(len(guesses), score))

print("Game over. Your final score was {}".format(score))