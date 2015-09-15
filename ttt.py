def draw_board(board):
	rows = []
	for i in range(3):
		rows+= [" "+board[i][0]+" | "+board[i][1]+" | "+board[i][2]]
	print(rows[0])
	print("---|---|---")
	print(rows[1])
	print("---|---|---")
	print(rows[2])
	print ()

def initialize(ch):
	board=[[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
	draw_board(board)
	print("you are player", ch)
	return board


# check_ending() checks whether a player has got 3-in-a-row
def check_ending(board):
	for i in range(3):
		if board[i][0]==board[i][1]==board[i][2]!=' ': return True
		if board[0][i]==board[1][i]==board[2][i]!=' ': return True
	if board[0][0]==board[1][1]==board[2][2]!=' ': return True
	if board[2][0]==board[1][1]==board[0][2]!=' ': return True
	return False


# play_move() updates the board with the move, calls check_ending()
# to see whether a player wins, and returns True or False accordingly
def play_move(board, move, ch):
	board[int(move[0])][int(move[2])] = ch
	draw_board(board)
	if check_ending(board):
		print("Player", ch,  "wins!")
		return True
	else: return False
	
	
	