
import random
WORDS=("python","jumble","easy","password","answer","iPhone")
word=random.choice(WORDS)
correct=word
jumble=""
while word:
 position= random.randrange(len(word))
 jumble += word[position]
 word = word[:position]+word[(position+1):]

print("The jumble is:",jumble)
guess=input("\n your guess:")
while guess!=correct and guess !="":
 print("很遗憾没猜对.'")
 guess = input("your guess:")
if guess==correct:
   print("恭喜你猜对了\n")
input("\n\npress the enter key to exit.")