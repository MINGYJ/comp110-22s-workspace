"""A Wordle Game"""

__author__ = "730486611"

secret_word: str="python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji_box: str=""

guess_word: str=input("What is your 6-letter guess?")

while len(guess_word)!=6:
    guess_word=input("That was not 6 letters! Try again:")

count_index: int=0
perfect_flag: bool=True
while count_index < 6:
    if(guess_word[count_index]==secret_word[count_index]):
        emoji_box+=GREEN_BOX
    else:
        perfect_flag=False
        yellow_flag: bool = False
        secret_index: int = 0
        while (secret_index < 6) and (not yellow_flag):
            if (guess_word[count_index]==secret_word[secret_index]):
                emoji_box+=YELLOW_BOX
                yellow_flag=True
            secret_index+=1
        if(not yellow_flag):
            emoji_box+=WHITE_BOX
    count_index+=1
print(emoji_box)
if(perfect_flag):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
