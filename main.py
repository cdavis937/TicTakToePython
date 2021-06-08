board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]

#Who's turn 
current_player = "X"

#If game still going 
game_still_going = True

#Who wins 
winner = None

#Count number of turns 
count = 0

#Prints the board to the console
def display_board(): 
  print( board[0] + "|" + board[1] + "|" + board[2])
  print( board[3] + "|" + board[4] + "|" + board[5])
  print( board[6] + "|" + board[7] + "|" + board[8])

#Plays a game of tik tac toe
def play_game():

  #While the game is still going
  while game_still_going:
    

    #Display the board
    display_board()

    #Gives player a chance to take their turn
    handle_turn(current_player)

    #Checks if there was a winner at all
    check_if_game_over()

    #Changes whos turn it is
    flip_player()

  #The game has ended
  if winner == "X" or winner == "O":
    print(winner + " won!")
  else:
    print("It's a tie!")

#Checks to see if the game is over
def check_if_game_over():
  check_if_win()
  check_if_tie()

#Checks to see if a player won
def check_if_win():
 
  global winner
 
  #check rows
  row_winner = check_rows()
  #check cols
  col_winner = check_cols()
  #check diag
  diag_winner = check_diag()

  if row_winner:
    #There was a winner
    winner = row_winner
  elif col_winner:
    #There was a winner
    winner = col_winner
  elif diag_winner:
    #There was a winner
    winner = diag_winner
  else:
    #There was no winner
    winner = None

  return

#Checks to see if a player won in any of the rows
def check_rows():
  
  #Setup global varaibles
  global game_still_going

  #Check if any of the row have the same non empty value
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board [5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"

  #If anyone one then end the game
  if row1 or row2 or row3:
    game_still_going = False

    #Return the winner
    if row1:
      return board[0]
    elif row2:
      return board[3]
    elif row3:
      return board[6]
  
  return

#Checks to see if a player won in any column
def check_cols():

  #Setup global varaibles
  global game_still_going

  #Check if any of the columns have the same non empty value
  col1 = board[0] == board[3] == board[6] != "-"
  col2 = board[1] == board[4] == board [7] != "-"
  col3 = board[2] == board[5] == board[8] != "-"

  #If anyone one then end the game
  if col1 or col2 or col3:
    game_still_going = False

    #Return the winner
    if col1:
      return board[0]
    elif col2:
      return board[1]
    elif col3:
      return board[2]

  return

#Checks to see if a player won is diagonal direction
def check_diag():
  
  #Setup global varaibles
  global game_still_going

  #Check if any of the row have the same non empty value
  diag1 = board[0] == board[4] == board[8] != "-"
  diag2 = board[2] == board[4] == board [6] != "-"

  #If anyone one then end the game
  if diag2 or diag1:
    game_still_going = False

    #Return the winner
    if diag1:
      return board[0]
    elif diag2:
      return board[2]
  
  return
  
#Checks to see if there is a tie
def check_if_tie():
  
  global game_still_going

  global count

  count += 1

  if(count == 9):
    game_still_going = False
  
  
  return

#Flips which players turn it is
def flip_player():

  global current_player

  if current_player == "X":
    current_player = "O"
  else:
    current_player = "X"

  return

#Handles one turn in the tik tak toe game
def handle_turn(player):
  
  global board

  new_position = False
  
  while not(new_position):

    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    if position <= 8 and position >= 0:
      if board[position] != "O" and board[position] !=  "X":
        new_position = True
      else:
        print("Pick a new position")
    else:
      "Please enter position 1-9:"

    
  
  board[position] = player

  return

#Play the game
play_game()

#board
#display board
#play game
#handle turn
#check win
  #check rows
  #check cols
  #check diag
#check tie
#flip