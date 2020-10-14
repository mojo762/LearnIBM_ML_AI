#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
#compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
from os import system
new_game=True


while new_game == True:
    p1_win=False
    p2_win=False
    Tie = False
    
    name1=input('What is your name Player 1?  ')
    player1=input('Rock, Paper, or Scissors?  ')
    system('cls')
    print('========================================')
    print('')
    print('Ready for the other Player')
    print('')
    print('========================================')
    name2=input('What is your name Player 2?  ')
    player2=input('Rock, Paper, or Scissors?  ')
    system('cls')
    print('========================================')
    print('')
    print(name1, 'selected ',player1)
    print(name2, 'selected ',player2)
    print('')
    print('========================================')
    player1=player1.lower()
    player2=player2.lower()
    #print(player1, player2)
    #print(player1[0], player2[0])

    #Tie case
    if player1[0] == player2[0]:
        Tie = True
    #Rock beats scissors: Player 1 wins
    elif player1[0]=='r'and player2[0]=='s':
        p1_win=True
    #Rock beats scissors: Player 2 wins
    elif player1[0]=='s'and player2[0]=='r':
        p2_win=True
    #Scissors beats paper: player 1 wins
    elif player1[0]=='s'and player2[0]=='p':
        p1_win=True
    #Scissors beats paper: player 2 wins
    elif player1[0]=='p'and player2[0]=='s':
        p2_win=True
    #Paper beats Rock: player 1 wins
    elif player1[0]=='p'and player2[0]=='r':
        p1_win=True
    #Paper beats Rock: player 2 wins
    elif player1[0]=='r'and player2[0]=='p':
        p2_win=True
    else:
        print('invlaid selection......Try Again!!!')
        break
    if p1_win == True:
        print('========================================')
        print('')
        print(name1,'  Wins!!!')
        print('========================================')
        print('')
    if p2_win == True:
        print('========================================')
        print('')
        print(name2,'  Wins!!!')
        print('========================================')
        print('')
    if Tie == True:
        print('========================================')
        print('')
        print('It is a TIE')
        print('========================================')
        print('')
    again=input('Do you want to play again? [Y/N]  ' )
    again=again.lower()
    if again == 'n':
        print('Thanks for playing!!')
        break
