# Brandon Brien
# 10079883
# CPSC 441, Assignment 2
# Due February 24th, 2015
#
# This is the server side of the tic-tac-toe game
# Assumptions: 
# 	- the user enters a valid move
#	
# Known Bugs: None
#
# All the board drawing functions and logic checking
# functions were borrowed from Professor Li.
#
# Learned about the use of pickle, and how it works from:
# http://stackoverflow.com/questions/24423162/how-to-send-an-array-over-a-socket-in-python
# *could have also used str.encode because the messages being
#  sent are just strings



import socket, pickle, ttt
	
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host,port))

#Variables
our_character = "O"
their_character = "X"
our_board = ttt.initialize(our_character)
finished = False

#Waits for client connection
s.listen(5)

while True:
    c, addr = s.accept()
	
	# While there isn't a winner, receive & play clients move,
	# then play & send ours, then loop
    while(finished == False):
         their_move = pickle.loads(c.recv(1024))
         finished = ttt.play_move(our_board, their_move, their_character)
		 
         if(finished == True):
             break
	
         our_move = input("Enter a move in the format 'X Y': ")
         finished = ttt.play_move(our_board, our_move, our_character)
         c.send(pickle.dumps(our_move))
		 
    c.close()
    break
