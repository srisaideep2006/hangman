import random
from words import *

chosen_word = random.choice(word_list)
word_length= len(chosen_word)

lives = 6

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

display = []
for _ in range(word_length):
    display += "_"  
print(display)    

endgame = False
while not endgame:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            endgame = True
            print("You lose")


    print(display)    

    if "_" not in display:
        endgame = True
        print("You win.")

    print(stages[lives])    