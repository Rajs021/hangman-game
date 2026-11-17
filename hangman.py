import random


MAX_MISTAKES = 6
WORDS = (
    "apple",
    "bridge",
    "candle",
    "diamond",
    "elephant",
    "freedom",
    "garden",
    "horizon",
    "island",
    "journey",
    "lantern",
    "mountain",
    "notebook",
    "ocean",
    "puzzle",
    "rainbow",
    "sunshine",
    "treasure",
    "umbrella",
    "volcano",
)

HANGMAN_STAGES = (
    (
        "  +---+\n"
        "  |   |\n"
        "      |\n"
        "      |\n"
        "      |\n"
        "=========",
    ),
    (
        "  +---+\n"
        "  |   |\n"
        "  O   |\n"
        "      |\n"
        "      |\n"
        "=========",
    ),
    (
        "  +---+\n"
        "  |   |\n"
        "  O   |\n"
        "  |   |\n"
        "      |\n"
        "=========",
    ),
    (
        "  +---+\n"
        "  |   |\n"
        "  O   |\n"
        " /|   |\n"
        "      |\n"
        "=========",
    ),
    (
        "  +---+\n"
        "  |   |\n"
        "  O   |\n"
        " /|\\  |\n"
        "      |\n"
        "=========",
    ),
    (
        "  +---+\n"
        "  |   |\n"
        "  O   |\n"
        " /|\\  |\n"
        " /    |\n"
        "=========",
    ),
    (
        "  +---+\n"
        "  |   |\n"
        "  O   |\n"
        " /|\\  |\n"
        " / \\  |\n"
        "=========",
    ),
)


def display_game(word, guessed_letters, mistakes):
    """Display the current gallows, word progress, and guessed letters."""
    print(HANGMAN_STAGES[mistakes])
    masked_word = " ".join(
        letter.upper() if letter in guessed_letters else "_" for letter in word
    )
    print(f"\nWord: {masked_word}")
    print(f"Guessed letters: {' '.join(sorted(guessed_letters)).upper() or '-'}")
    print(f"Incorrect guesses remaining: {MAX_MISTAKES - mistakes}")


def play_game(word=None):
    """Run one round of Hangman. A word can be supplied for predictable tests."""
    word = (word or random.choice(WORDS)).lower()
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Hangman!")

    while mistakes < MAX_MISTAKES:
        display_game(word, guessed_letters, mistakes)
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
            print("Please enter a single English letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess.upper()}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            mistakes += 1
            print(f"Sorry, '{guess.upper()}' is not in the word.")
        else:
            print(f"Good guess! '{guess.upper()}' is in the word.")

        if all(letter in guessed_letters for letter in word):
            display_game(word, guessed_letters, mistakes)
            print(f"\nYou win! The word was {word.upper()}.")
            return True

    display_game(word, guessed_letters, mistakes)
    print(f"\nGame over! The word was {word.upper()}.")
    return False


def main():
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print("\nGame ended. Thanks for playing!")


if __name__ == "__main__":
    main()
