hiddenWord = "MARYLAND"
GuessedLetters = ""

strikes = 5 


while strikes > 0:

    guess = input("\nEnter a letter: ")
    guess = guess.upper()

    if guess in hiddenWord:
        print(f"Good Job! There is {guess} in the hidden word. You have {strikes} turn(s) left.")
    else:
        strikes -= 1
        print(f"Incorrect! There is no {guess} in the hidden word. {strikes} turn(s) left.")
    
    GuessedLetters = GuessedLetters + guess
    wrongLetterCount = 0

    for letter in hiddenWord:
        if letter in GuessedLetters:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1

    if wrongLetterCount == 0:
        print(f"\nCongratulations! The secret word was: {hiddenWord}. You won!")
        break

else: 
    print("\nSorry, no more trys")