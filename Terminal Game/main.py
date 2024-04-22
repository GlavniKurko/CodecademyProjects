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
        user1_input = str(input("User1 Pick a Square: "))
        user1_moves.append(user1_input)
        user2_input = str(input("User2 Pick a Square: "))
        user2_moves.append(user2_input)

        update_board(user1_moves, user2_moves)






    



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