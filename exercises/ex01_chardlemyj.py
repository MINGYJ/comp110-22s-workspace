"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730486611"

word: str = input("Enter a 5-character word: ")
if(len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
ch: str = input("Enter a single character: ")
if(len(ch) != 1):
    print("Error: Character must be a single character.")
    exit()
count: int = 0
print("Searching for " + ch + " in " + word)
if(word[0] == ch):
    print(ch + " found at index " + str(0))
    count = count + 1
if(word[1] == ch):
    print(ch + " found at index " + str(1))
    count = count + 1
if(word[2] == ch):
    print(ch + " found at index " + str(2))
    count = count + 1
if(word[3] == ch):
    print(ch + " found at index " + str(3))
    count = count + 1
if(word[4] == ch):
    print(ch + " found at index " + str(4))
    count = count + 1
if count == 0:
    print("No instances of " + ch + " found in " + word)
else:
    if(count == 1):
        print(str(count) + " instance of " + ch + " found in " + word)
    else:
        print(str(count) + " instances of " + ch + " found in " + word)
