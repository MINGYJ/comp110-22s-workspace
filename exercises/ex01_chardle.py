"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "9842615731"

word: str=input("Enter a 5-character word:")
if(len(word)!=5):
    print("Error: Word must contain 5 characters")
    quit()
ch: str=input("Enter a single character:")
if(len(ch)!=1):
    print("Error: Character must be a single character.")
    quit()
count: int=0
print("Searching for e in hello")
for x in range(5):
    if(word[x]==ch):
        print(ch+" found at index "+str(x))
        count=count+1
if count==0:
    print("No instance of "+ch+" found in "+word)
else:
    print(str(count)+" instance of "+ch+" found in "+word)





