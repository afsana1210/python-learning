#from IPython.display import clear_output
import random
def display_board(board):
 
 print board[7]+'|'+board[8]+'|'+board[9]
 print board[6]+'|'+board[5]+'|'+board[4]
 print board[3]+'|'+board[2]+'|'+board[1]



#test_board=['#','x','o','x','o','x','o','x','o','x']
#test_board=[' ']*10
#display(test_board)

def player_input():
  
  marker=''

  while not (marker =='x' or marker =='o'):
    marker=input('player1,choose x or o :')

  if marker =='x':
   return ('x','o') 
  else:
    return('o','x')  

#player_input()

def place_marker(board,marker,position):
  board[position]=marker


#place_marker(test_board,'$',8)  
  


def win_chk(board,marker):
  return ((board[7]==marker and board[8]==marker and board[9]==marker) or
          (board[6]==marker and board[5]==marker and board[4]==marker) or
          (board[3]==marker and board[2]==marker and board[1]==marker) or 
          (board[9]==marker and board[4]==marker and board[1]==marker) or
          (board[7]==marker and board[6]==marker and board[3]==marker) or
          (board[8]==marker and board[5]==marker and board[2]==marker) or
          (board[9]==marker and board[5]==marker and board[3]==marker) or
          (board[7]==marker and board[5]==marker and board[1]==marker))

#chk_won(test_board,'x')          

def choose_first():
   flip=random.randint(0,1)

   if flip==0:
     return 'player1'
   else:
     return 'player2'


def space_chk(board,position):
  return board[position] ==' '


def player_choice(board):
  position=0

  while position not in [1,2,3,4,5,6,7,8,9] or not space_chk(board,position):
    position=input('choose a position (1-9) :')
    return position


def full_board_chk(board):
    for i in range(1,10):
      if space_chk(board,i):
        return False

    return True   

def replay():
  choice=input('play again? enter yes or no')
  return choice=='yes'              


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_chk(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_chk(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_chk(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_chk(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break