import random


def main():
    while True:
        words = ["python", "golang", "java", "assembly", "haskel", "emoji"]
        chosen_word = random.choice(words).lower()
        player_guess = None
        guessed_letters = []
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("*")
        joined_word = None
        chances = 10
        attempts = chances - 1
        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(
                    input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except:
                print("please enter valid input and try again")
                continue
            else:
                if not player_guess.isalpha():
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1:
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters:
                    print("You have already guessed that letter. Please try again.")
                    continue

            guessed_letters.append(player_guess)

            for pos, letter in enumerate(chosen_word):
                if player_guess == letter:
                    word_guessed[pos] = player_guess

            if player_guess not in chosen_word:
                attempts -= 1

        if "-" not in word_guessed:
            print(("\nCongratulations! {} was the word").format(chosen_word))
        else:
            print(("\nUnlucky! The word was {}.").format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            break


if __name__ == "__main__":
    main()
