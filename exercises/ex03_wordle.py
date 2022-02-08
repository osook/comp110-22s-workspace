"""Exercise 3 wordle!"""

__author__ = "730521185"


def contains_char(word_search:str, char_search:str)-> bool:
    """Checks if word contains a character."""
    assert len(char_search) == 1
    i: int = 0
    while i < len(word_search):
        if word_search[i] == char_search:
            return True
        else:
            i += 1
    else:
        return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess:str, secret:str)-> str:
    """Takes the guessed word and the secret word and emojifies the result."""
    assert len(guess) == len(secret)
    emoji: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) == False:
                    emoji += WHITE_BOX
            else:
                    emoji += YELLOW_BOX
        i += 1
    return emoji

def input_guess(expect_length:int)-> str:
    """Ensures user puts in word with correct length."""
    guess: str = input(f"Enter a { expect_length } character word: ")
    while len(guess) != expect_length:
        guess = input(f"That wasn't { expect_length } chars ! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    status: bool = False
    secret: str = "codes"
    while turn < 6 and status == False:
        print(f"=== Turn { turn }/6 ===")
        guess_word = input_guess(5)
        print(emojified(guess_word, secret))
        if guess_word == secret:
            status = True
        else:
            turn += 1
    if status == True:
        print(f"You won in { turn }/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()