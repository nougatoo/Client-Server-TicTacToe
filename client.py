# Brandon Brien
#
# This is the client side of the tic-tac-toe game
# Assumptions: 
#	 - the user enters a valid move
# 	- the server program is already running
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


import socket, pickle, fileinput, ttt, time


# Setting up the socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

#Variables
our_character = "X"
their_character = "O"
our_board = ttt.initialize(our_character)
finished = False

# Connect through a port and host
s.connect((host,port))


# While there is no winner, play & send our move,
# then receive & play servers move, loop
while(finished == False):
     our_move = input("Enter a move in the format 'X Y': ")
     finished = ttt.play_move(our_board, our_move, our_character)
     #Now we've played our move and we need to send the board to the server

     s.send(pickle.dumps(our_move))
     if (finished == True):
         break

     their_move = pickle.loads(s.recv(1024))
     finished = ttt.play_move(our_board, their_move, their_character)


time.sleep(1)
s.close()
# Socket is not closed on client side because both server and client
# programs end and the socket is closed on the server side
