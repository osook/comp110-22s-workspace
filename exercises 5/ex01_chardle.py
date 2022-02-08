""""EX01 - Chardle - A cute step towards Wordle."""

__author__ = 730521185

five_word: str = input("Enter a 5-character word: ")

if len(five_word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()


one_word: str = input("Enter a single character: ")

if len(one_word) != 1:
    print("Error: Character must be a single character.")
    exit()

count: int = 0


print("Searching for " + one_word + " in " + five_word)  

if one_word == five_word[0]:
    print(one_word + " found at index 0")
    count = count + 1
if one_word == five_word[1]:
    print(one_word + " found at index 1")
    count = count + 1
if one_word == five_word[2]:
     print(one_word + " found at index 2")
     count = count + 1
if one_word == five_word[3]:
     print(one_word + " found at index 3")
     count = count + 1
if one_word == five_word[4]:
     print(one_word + " found at index 4")
     count = count + 1

if count == int(0):
    print("No instances of " + one_word + " found in " + five_word)
else:
    if count == int(1):
        print("1 instance of" + one_word + " found in " + five_word)
    if count == int(2):
        print("2 instances of " + one_word + " found in " + five_word)
    if count == int(3):
        print("3 instances of " + one_word + " found in " + five_word)
    if count == int(4):
        print("4 instances of " + one_word + " found in " + five_word)
    if count == int(5):
        print("5 instances of " + one_word + " found in " + five_word)

