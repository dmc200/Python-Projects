game =  [[0,0,0],
		 [0,0,0],
		 [0,0,0],]

def game_board(game):
	print("   0  1  2")
	for count,row in enumerate(game): 
		print(count,row)


## Tic-Tac-Toe:
game_board(game)
game[0][1] = 1
game_board(game)
