#the game shall require the kids to keep guessing the name of their county
#we can also ensure that the kids will only win after trying a couple number of times without losing
secret_word = "MAKUENI"
guess = ""
#set the number of guessing times
guessCount = 0
#set the limit
guessLimit = 3
#throw on quess limit remaining
outOfGuesses = False
while guess != secret_word and not(outOfGuesses):
    if guessCount < guessLimit:
        guess = input("Enter guess capital letters: ")
#Increment the guesses
        guessCount += 1
    else:
        outOfGuesses = True
if outOfGuesses:
    print("Out of Guesses, YOU LOSE")
else:
    
    print("You win")
