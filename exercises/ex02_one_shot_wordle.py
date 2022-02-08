"""EX02 one shot wordle."""

__author__ = "730521185"

secret: str = ("trail")

guess: str = input(f"What is your { len(secret) }-letter guess? ")

while len(guess) != len(secret):  #checking if the length of the guessed word matches the secret word
    guess = input(f"That was not { len(secret) } letters! Try again: ")

index: int = 0

emoji: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while index < len(secret):
    if guess[index] == secret[index]: 
        emoji = emoji + GREEN_BOX  #if guessed character matches secret character it will print a green emoji
    else:
        match: bool = False
        check: int = 0
        while match == False and check < len(secret):
            if guess[index] == secret[check]:  #checks if the characters in the guessed word matches any in the secret word
                match = True
            else:
                check = check + 1  #to make sure the while loop ends
        if match == True: 
            emoji = emoji + YELLOW_BOX  #if the character matches any in the secret word it will print an yellow emoji for that spot
        else: 
            emoji = emoji + WHITE_BOX  #if the character has no common ones with the secret word it will print a white emoji
    index = index + 1  #to make sure the while loop ends
        
print(emoji)


if guess == secret:  #if guess is correct
    print ("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
