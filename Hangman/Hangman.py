import random
import english_words


WORD_LENGTH = 8

word_list = []
word = []
guessed_letters = []
chosen_word = ""

person = [[' ', ' O ',' '],
         ['/', ' | ', "\\"],
         [' ', '|', '|']]
guess = " "
valid_guess = False
has_won = False
######################INIT###################
for i in english_words.english_words_lower_set:
    if len(i) == WORD_LENGTH:
        word_list.append(i)
for j in range(WORD_LENGTH):
    word.append("_")
chosen_word = random.choice(word_list)
#print(chosen_word)
##############################################

def PrintWord():
    for letter in word:
        print(letter, end=" ")
    print() #stops printing on the same line after for loop is done

def PrintPerson():
    for line in person:
        for q in line:
            print(q, end=" ")
        print()

def PrintGuesses():
    for guess in guessed_letters:
        print(guess, end=" ")
    print()

def LoseALife():
    for lineIndex, line in enumerate(reversed(person)):
        for index, limb in enumerate(reversed(line)):
            if limb != ' ':
                person[2-lineIndex][2-index] = " " #the "2 - " Helps the lives get taken right to left
                break
        if limb != ' ':
            break

while not has_won:
    PrintPerson()
    print("Incorrect Guessed Letters: ")
    PrintGuesses()
    print("Word: " )
    PrintWord()
    valid_guess = False
    while not valid_guess: #ensures same letter can't be guessed twice
        guess = input("What Letter Would You Like To Guess? ").lower()
        if guess in guessed_letters or len(guess) != 1:
            print("Invalid Guess")
        else:
            valid_guess = True
##INVALID GUESS CHECK
    if not guess in chosen_word:
        guessed_letters.append(guess)
        LoseALife()
##VALID GUESS CHECK
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            word[index] = guess
##WIN CHECK
    if (''.join(word)) == chosen_word: #compares the progress of the player with the word they're trying to guess
        print("Congrats, You Win!")
        print("The Word Was:",''.join(word) )
        has_won = True
        exit()

##LOSE CHECK
    if (all(i == person[0] for i in person)):
        print("Sorry, You Lose!")
        print("The Word Was:", chosen_word)
        exit()












