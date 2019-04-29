#from IPython.display import clear_output

def display(board):
 
 print board[7]+'|'+board[8]+'|'+board[9]
 print board[6]+'|'+board[5]+'|'+board[4]
 print board[3]+'|'+board[2]+'|'+board[1]



test_board=['#','x','o','x','o','x','o','x','o','x']
#test_board=[' ']*10
display(test_board)

def player_input():
  
  marker=''

  while not (marker =='x' or marker =='o'):
    marker=input('player1,choose x or o :')

  if marker =='x':
   return ('x','o') 
  else:
    return('o','x')  

player_input()

def place_marker(board,marker,position):
  board[position]=marker


place_marker(test_board,'$',8)  
  


def chk_won(board,marker):
  return ((board[7]==marker and board[8]==marker and board[9]==marker) or
          (board[6]==marker and board[5]==marker and board[4]==marker) or
          (board[3]==marker and board[2]==marker and board[1]==marker) or 
          (board[9]==marker and board[4]==marker and board[1]==marker) or
          (board[7]==marker and board[6]==marker and board[3]==marker) or
          (board[8]==marker and board[5]==marker and board[2]==marker) or
          (board[9]==marker and board[5]==marker and board[3]==marker) or
          (board[7]==marker and board[5]==marker and board[1]==marker))

chk_won(test_board,'x')          
              