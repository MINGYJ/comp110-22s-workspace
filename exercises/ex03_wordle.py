"""A wordle game with several defined functions."""

__author__ = "730486611"


def contains_char(secret: str, key: str) -> bool:
    """Searching whether the key char is in secret string."""
    assert len(key) == 1
    flag: bool = False
    count: int = 0
    while(count < len(secret) and not flag):
        if(key == secret[count]):
            return True
        count += 1
    return flag


def emojified(secret: str, guess: str) -> str:
    """Get the result of comparing two strings."""
    emoji_box: str = ""
    count: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    while count < len(secret):
        if(guess[count] == secret[count]):
            emoji_box += GREEN_BOX
        else:
            if(contains_char(secret, guess[count])):
                emoji_box += YELLOW_BOX
            else:
                emoji_box += WHITE_BOX 
        count += 1
    return emoji_box


def input_guess(str_length: int) -> str:
    """Make the sure the input it suitable."""
    guess_word: str = input(f"Enter a {str_length} character word: ")
    while(len(guess_word) != str_length):
        guess_word = input(f"That wasn't {str_length} chars! Try again: ")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    times: int = 0
    while(times < 6):
        print(f"=== Turn {times + 1}/6 ===")
        guess_word: str = input_guess(len("codes"))
        print(emojified("codes", guess_word))
        if(guess_word == "codes"):
            print(f"You won in {times+1}/6 turns!")
            break
        times += 1
    print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()