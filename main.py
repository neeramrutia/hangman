import random
from words import word_list
from asciiart import logo
choose=random.choice(word_list)
length=len(choose)
endofgame=False
lives=6
display=[]
print(logo)
for i in range(length):
    display += "_"

while not endofgame:
    guess=input("guess a letter :").lower()

    if guess in display:
        print(f"you have already guessed {display}")
    for i in range (length):
        letter=choose[i]
        if choose[i]==guess:
            display[i]=letter      
    if guess not in choose:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives =lives - 1
        if lives == 0:
            endofgame = True
            print(choose)
            print("You lose.")

    print(f"{' '.join(display)}")
    if "_" not in display:
        endofgame = True
        print("You win.")
    from asciiart import stages
    print(stages[lives])            
