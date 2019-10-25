import random, itertools

def win(current_game):
	# Horizontal
	for row in game: 
		if row.count(row[0]) == len(row) and row[0] != 0:
			message = print(f"Player {row[0]} is the winner horizontally(--)!")
			return message

	# Diag Winner
	diags = []

	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		message = print(f"Player {row[0]} is the winner diagonally (/)!")
		return message

	diags = []

	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		message = print(f"Player {row[0]} is the winner diagonally (\\)!")
		return message


	# Vert Winner 
	for col in range(len(game)):
		check = []

		for row in game:
			check.append(row[col])

		if check.count(check[0]) == len(check) and check[0] != 0:
			message = print(f"Player {check[0]} is the winner vertically (|)!")
			return message


def game_board(game, player, row, column, just_display=False):
	try: 
		print("   0  1  2")
		if not just_display:
			game[row][column] = player
		for count, row in enumerate(game):
			print(count, row)
		return game
	except IndexError as e:
		print("Error: make sure you input row/column as 0 1 or 2?", e)
	except Exception as e: 
		print("Something went very wrong!", e)


play = True

while play: 
	print("Welcome to Tic-Tac_Toe! ")
	game =  [[0, 0, 0],
		 	 [0, 0, 0],
		 	 [0, 0, 0]]
	game_won = False
	current_player = random.randint(1,2)
	
	while not game_won:
		if current_player == 1:
			print("Player 1 is playing . . . ")
			print("   0  1  2")
			for x, y in enumerate(game):
				print(x, y)
			column_choice = int(input(f" Player {current_player} what column do you want to choose? (0,1,2) "))
			row_choice = int(input(f" Player {current_player} what row do you want to choose? (0,1,2) "))
			game_map = game_board(game, current_player, row_choice, column_choice, False)
			message = win(game_map)

			if message:
				print(message)
				print(game_map)
				game_won = True
			else:
				current_player = 2

		else current_player == 2: 
			print("Player 2 is playing . . . ")
			print("   0  1  2")
			for x, y in enumerate(game):
				print(x, y)
			column_choice = int(input(f" Player {current_player} what column do you want to choose? (0,1,2) "))
			row_choice = int(input(f" Player {current_player} what row do you want to choose? (0,1,2) "))
			game_map = game_board(game, current_player, row_choice, column_choice, False)
			message = win(game_map)

			if message:
				print(message)
				print(game_map)
				game_won = True
			else:
				current_player = 1

	again = input("Do you want to play again? y/n").lower()
	if 	again == 'y':
		play = True
	else: 
		play = False