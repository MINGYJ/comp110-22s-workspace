"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "9842615731"

word: str=input("Enter a 5-character word:")
ch: str=input("Enter a single character:")
count: int=0
print("Searching for e in hello")
if(len(word)!=5):
    print("Error: Word must contain 5 characters")
    quit()
if(len(ch)!=1):
    print("Error: Character must be a single character.")
    quit()
for x in range(5):
    if(word[x]==ch):
        print(ch+" found at index "+str(x))
        count=count+1
print(str(count)+" instance of "+ch+" found in "+word)





