""" a magic eightball oracle of truth about future"""

from random import randint

input("Ask yes or no question: ")

response: int=randint(0,3)

if response==0:
    print("Yes, definitely!")
elif(response==1):
    print("Looking hopefully!")
elif(response==2):
    print("Ask again Later")
else:
    print("No way, not a chance")
