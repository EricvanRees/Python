
# coding: utf-8

# In[ ]:


'''Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

while True: 
    usr_command1 = input("User1, Enter Rock, Paper, Scissors or quit: ")
    usr_command2 = input("User2, Enter Rock, Paper, Scissors or quit: ")
    print("User1 typed " + usr_command1 + ", User2 typed " + usr_command2)
    if usr_command1 == "quit" or usr_command2 == "quit":
        break
    elif usr_command1 == usr_command2:
        print("It´s a tie!")
    elif usr_command1 == "Rock" and usr_command2 == "Scissors":
        a = input("User1 wins, want to start a new game? Y/N")
        if a == "Y":
            continue
        else:
            break
    elif usr_command1 == "Rock" and usr_command2 == "Paper":
        a = input("User2 wins, want to start a new game? Y/N")
        if a == "Y":
            continue
        else:
            break
    elif usr_command1 == "Scissors" and usr_command2 == "Rock":
        a = input("User 2 wins, want to start a new game? Y/N ")
        if a == "Y":
            continue
        else:
            break
    elif usr_command1 == "Scissors" and usr_command2 == "Paper":
        a = input("User1 wins, want to start a new game? Y/N ")
        if a == "Y":
            continue
        else:
            break
    elif usr_command1 == "Paper" and usr_command2 == "Rock":
        a = input("User1 wins, want to start a new game? Y/N ")
        if a == "Y":
            continue
        else:
            break
    else:
        if usr_command1 == "Paper" and usr_command2 == "Scissors":
            a = input("User2 wins, want to start a new game? Y/N ")
        if a == "Y":
            continue
        else:
            break
        

