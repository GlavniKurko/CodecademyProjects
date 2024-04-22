import sys

game_over = False
gameboard = {1: '''          
                         |           |             
                         |           |             
                  1      |     2     |    3     
             ____________|___________|__________
                         |           |          
                         |           |          
                  4      |     5     |    6     
            _____________|___________|__________
                         |           |
                         |           |
                  7      |     8     |    9
             ____________|___________|__________
                         |           |
                         |           |'''}

def checkWinner(user1, user2):
    global game_over
    global gameboard
    gameboard_string = gameboard[1]
    winning_positions = {1: ["1","2","3"], 2: ["1","5","9"], 3: ["1","4","7"], 4: ["2","5","8"], 5: ["3","6","9"], 6: ["3","5","7"], 7: ["4","5","6"], 8: ["7","8","9"]}
    if len(user1) < 3 or len(user2) < 3:
        update_board(user1, user2)
    elif len(user1) == 3 or len(user2) == 3:
        user1_list = user1
        user2_list = user2
        user1_list.sort()
        user2_list.sort()
        for x in winning_positions.values():
            if user1_list == x:
                print("User1 has won!")
                update_board(user1, user2)
                sys.exit()
            elif user2_list == x:
                print("User2 has won!")
                update_board(user1, user2)
                sys.exit()
            else:
                pass
        update_board(user1, user2)
    elif len(user1) == 4 or len(user2) == 4:
        user1_list_2 = user1
        user2_list_2 = user2
        for x in winning_positions.values():
            if x[0] in user1_list_2 and x[1] in user1_list_2 and x[2] in user1_list_2:
                print("User1 has won!")
                update_board(user1_list_2, user2_list_2)
                sys.exit()
            elif x[0] in user2_list_2 and x[1] in user2_list_2 and x[2] in user2_list_2:
                print("User2 has won!")
                update_board(user1_list_2, user2_list_2)
                sys.exit()
            else:
                pass
    elif len(user1) == 5:
        user1_list_2 = user1
        user2_list_2 = user2
        for x in winning_positions.values():
            if x[0] in user1_list_2 and x[1] in user1_list_2 and x[2] in user1_list_2:
                print("User1 has won!")
                update_board(user1_list_2, user2_list_2)
                sys.exit()
            else:
                print("The Game is a draw!")
                update_board(user1_list_2, user2_list_2)
                sys.exit()
    else:
        user1_list_2 = user1
        user2_list_2 = user2             
        print("The Game is a draw!")
        update_board(user1_list_2, user2_list_2)
        sys.exit()

def update_board(user1, user2):
    global gameboard
    gameboard_string = gameboard[1]
    for x in user1:
        gameboard_string = gameboard_string.replace(x, "X")
    for x in user2:
        gameboard_string = gameboard_string.replace(x, "O")
    
    print(gameboard_string)

def get_gameboard():
    global gameboard
    print(gameboard[1])

def main():
    global game_over
    get_gameboard()
    user1_moves = []
    user2_moves = []
    while game_over != True:
        user1_input = str(input("P1 Pick a Square: "))
        user1_moves.append(user1_input)
        checkWinner(user1_moves, user2_moves)
        user2_input = str(input("P2 Pick a Square: "))
        user2_moves.append(user2_input)
        checkWinner(user1_moves, user2_moves)

print(''' _____  _  ____     _____  ____  ____     _____  ____  _____  
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/  
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \    
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_   
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____|''')
user_input = input("Do you want to play a game of Tic-Tac-Toe? (Yes or no): ")
if user_input.lower() == "yes":
    main()
else:
    print("Maybe next time...")