def user_move(player, move):
    if move == "1" and player == 1:
        print('''
                             |            |           
                             |            |           
                     X       |      2     |    3      
                 ____________|____________|___________
                             |            |           
                             |            |           
                     4       |      5     |    6      
                 ____________|____________|___________          
                             |            |           
                             |            |           
                     7       |      8     |    9      
                 ____________|____________|___________
                             |            |
                             |            |
                             |            |''')

def gameboard():
    print('''
                         |            |           
                         |            |           
                 1       |      2     |    3      
             ____________|____________|___________
                         |            |           
                         |            |           
                 4       |      5     |    6      
             ____________|____________|___________          
                         |            |           
                         |            |           
                 7       |      8     |    9      
             ____________|____________|___________
                         |            |
                         |            |
                         |            |''')
def main():
    game_over = False
    user_moves = []
    gameboard()

    while game_over != True:
        user1_input = input("Enter a number: ")
        user_move(1, user1_input)

    



print(''' _____  _  ____     _____  ____  ____     _____  ____  _____  
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/  
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \    
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_   
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____|''')
user_input = input("Do you want to play a game of BlackJack? (Yes or no): ")
if user_input.lower() == "yes":
    main()
else:
    print("Maybe next time...")