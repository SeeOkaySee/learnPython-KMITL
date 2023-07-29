import random

# get user's value
usr = int(input("scissor(0),rock(1),paper(2): "))

# generate 0,1,2
opp = random.randint(0,3)

if usr == 0:
    if opp == 0:
        print("both play scissor, It is a draw!")
    elif opp == 1:
        print("PC plays rock, you lose!")
    else:
        print("PC plays paper, you won!")
elif usr == 1:
    if opp == 1:
        print("both play rocks, It is a draw!")
    elif opp == 0:
        print("PC plays scissor, you won!")
    else:
        print("PC plays paper, you lose!")
elif usr == 2:
    if opp == 2:
        print("both play paper, It is a draw!")
    elif opp == 0:
        print("PC plays scissor, you lose!")
    else:
        print("PC plays rock, you won!")
else:
    print("only 0,1,2 is allowed")