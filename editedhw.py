import random

def main():
    welcome = ['You have to guess a word',
               'within the letter limit',
               'go!'
               ]

    for line in welcome:
        print(line, sep='\n')

    

    play_again = True

    while play_again:
   

        words = ["hangman", "computer", "backpack", "pencil", "ruler",
                 "word", "code", "leave", "nylon", "toad",
                 "frog", "paper", "nerd", "sad", "cry",
                 "algebra", "children", "beat", "alive", "money"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None 
        guessed_letters = [] 
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") 
        joined_word = None 

        HANGMAN = (
"""
Y
""",
"""
YO
""",
"""
YOU
""",
"""
YOU A
""",
"""
YOU AR
""",
"""
YOU ARE
""",
"""
YOU ARE D
""",
"""
YOU ARE DE
""",
"""
YOU ARE DEA
""",
"""
YOU ARE DEAD
""",
"""
YOU ARE DEAD!
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except:
                print("That is not valid input. Please try again.")
                continue                
            else: 
                if not player_guess.isalpha(): 
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: 
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters: #
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess 
            if player_guess not in chosen_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: 
            print(("\nCongratulations! {} was the word").format(chosen_word))
        else:
            print(("\nUnlucky! The word was {}.").format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
