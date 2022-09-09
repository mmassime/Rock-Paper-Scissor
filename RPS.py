import random

botActions = [1, 2, 3]
actions = ["rock", "paper", "scissor"]

def winner(you, bot):
    # return 0 if even, 1 if you win, 3 if the bot win
    if you == bot:
        return 0
    elif you == 1 and bot == 2:
        return 2
    elif you == 1 and bot == 3:
        return 1
    elif you == 2 and bot == 1:
        return 1
    elif you == 2 and bot == 3:
        return 2
    elif you == 3 and bot == 1:
        return 2
    elif you == 3 and bot == 2:
        return 1

score = [0, 0]
while True:
    print("==================================================")
    print("score is " + str(score[0]) + " to " + str(score[1]))
    yourMove = input("chose your move : 1 rock, 2 paper, 3 scissor")
    botMove = random.choice(botActions)
    win = winner(int(yourMove), botMove)
    print ("you played : " + actions[int(yourMove)-1])
    print("the cpu played : " + actions[botMove - 1])

    if win == 1:
        print("you win!")
        score[0] += 1
    elif win == 2:
        print("the cpu win!")
        score[1] += 1
    else:
        print("No one win :( ")
    
    

        
        