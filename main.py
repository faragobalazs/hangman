import random
from hangman_art import logo
from hangman_words import word_list
from hangman_art import stages

print(logo)


# ------------------------------------------------------------------------------------- #

LIVES = 6

CHOSEN_WORD = random.choice(word_list)
WORD_LENGTH = len(CHOSEN_WORD)
PLACEHOLDER = ""
GAME_OVER = False
CORRECT_LETTERS = []
GUESSED_LETTERS = []

# ------------------------------------------------------------------------------------- #

# FOR LOOP FOR WORD TO GUESS
for position in range(WORD_LENGTH):
   PLACEHOLDER += "_"
print(f"\nWord to guess: " + PLACEHOLDER)


# MAIN GAME SYSTEM
while not GAME_OVER:
   print(f"\n{LIVES}/6 LIVES LEFT")
   guess = input(f"\nGuess a letter: ").lower()

   # IF YOU HAVE ALREADY GUESSED A LETTER
   if guess in GUESSED_LETTERS:
       print(f"You have already guessed {guess}.")
   GUESSED_LETTERS.append(guess)
   display = ""

   # CHECKING GUESS LETTERS AND ADDING TO THE WORD IF CORRECT
   for letter in CHOSEN_WORD:
       if letter == guess:
           display += letter
           CORRECT_LETTERS.append(guess)
       elif letter in CORRECT_LETTERS:
           display += letter
       else:
           display += "_"
   print(f"\nWord to guess: " + display)

   # IF GUESSED WORD IS NOT IN WORD, -1 LIVE
   if guess not in CHOSEN_WORD:
       print(f"\nYou guessed: {guess}, that is not in the word. You lose a life.")
   if guess not in CHOSEN_WORD:
       LIVES -= 1
       if LIVES == 0:
           GAME_OVER = True
           print(f"\nIT WAS {CHOSEN_WORD}! YOU LOSE!")

   # WINNING
   if "_" not in display:
       GAME_OVER = True
       print("\nYOU WIN!")

   # PRINTING STAGES
   print(stages[LIVES])


# ------------------------------------------------------------------------------------- #
# END OF CODE