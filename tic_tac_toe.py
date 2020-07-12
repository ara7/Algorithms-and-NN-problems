#Tic tac toe problem

#--Global variables ---
#Game board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"] #list 3x3

#If game is still going
game_still_going = True

#Who won
winner = None

#Whose turn is it
current_player = "X"
#display the board
def display_board():
  print(board[0] + "|" + board[1] + "|" + board[2] )
  print(board[3] + "|" + board[4] + "|" + board[5] )
  print(board[6] + "|" + board[7] + "|" + board[8] )


#play the game
def play_game():
  #display the board
  display_board()
  #handle the turn
  while game_still_going:
    handle_turn(current_player)
    check_if_game_over()

    #Flip to the other player
    flip_player()
  #the game has ended
  if winner =="X" or winner == "O":
    print('The winner is:' + winner)
  elif winner == None:
    print("Tie")


#handle the turn
def handle_turn(current_player):
  print("Player:" + current_player + "'s turn.")
  position = input("Choose a position from 1 to 9: ")

  valid = False
  while not valid:#this loop checks we are not overwriting a filled spot
    while position not in ["1","2","3","4","5","6","7","8","9"]:#if checks only one time,so we need to put in while loop
      position = input("Invalid input. Choose a position from 1 to 9: ")
    #string needs to be converted to int

    position = int(position) - 1
    #check that we are not over writing
    if board[position]=="-":
      valid = True
    else:
      print("Yo can't overwrite")


  board[position] = current_player#"X"
  display_board()

#check if there is win
  #check row, col and diagonals
def check_if_game_over():
  check_if_win()
  check_if_tie()

def check_if_win():
  #check row, col, diagonal
  #set up global variables
  global winner
  row_winner = check_rows()
  col_winner = check_cols()
  diag_winner = check_diagonals()

  if row_winner:
    #Won
    winner = row_winner
  elif col_winner:
    #Won
    winner = col_winner
  elif diag_winner:
    #Won
    winner = diag_winner
  else:
    #no win
    winner = None
  return

def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  #return winner x or o
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_cols():
  global game_still_going
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"
  if col_1 or col_2 or col_3:
    game_still_going = False
  #return winner x or o
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  return

def check_diagonals():
  global game_still_going
  diag_1 = board[0] == board[4] == board[8] != "-"
  diag_2 = board[2] == board[4] == board[6] != "-"

  if diag_1 or diag_2:
    game_still_going = False
  #return winner x or o
  if diag_1:
    return board[0]
  elif diag_2:
    return board[2]
  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return

play_game()

#check the tie
#flip players
