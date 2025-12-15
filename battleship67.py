import random
import string

GRID_SIZE = 10
SHIP_LENGTHS = [5, 4, 3, 2]

EMPTY = "🌊"
SHIP = "🚢"
HIT = "💥"
MISS = "❌"

#create board of just ocean
def create_board():
	return [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

#print board with letter columns and number rows
def print_board(board, hide_ships=False):
	col_labels = list(string.ascii_uppercase[:GRID_SIZE])
	print("   " + "  ".join(col_labels))
	for idx, row in enumerate(board):
		display_row = []
		for cell in row:
			if hide_ships and cell == SHIP:
				display_row.append(EMPTY)
			else:
				display_row.append(cell)
		print(f"{idx:2} " + " ".join(display_row))
	print()

#is the ship sunk or not
def is_ship_sunk(ship, board):
	return all(board[r][c] == HIT for r, c in ship)

#make sure letters input by player are understood as index by computer
def letter_to_index(letter):
	letter = letter.upper()
	if letter in string.ascii_uppercase[:GRID_SIZE]:
		return string.ascii_uppercase.index(letter)
	return -1

#let the player place their ships
def place_player_ships():
	board = create_board()
	ships = []

	print("Place your ships (row col h/v)")
	for length in SHIP_LENGTHS:
		valid = False
		while not valid:
			print_board(board)
			inp = input(f"Place ship of length {length}: ")
			try:
				parts = inp.split()
				row = int(parts[0])
				col = letter_to_index(parts[1])
				orient = parts[2].lower()
				coords = []

				if col == -1:
					print("Invalid column")
					continue

				if orient == "h" and col + length <= GRID_SIZE:
					coords = [(row, col+i) for i in range(length)]
				elif orient == "v" and row + length <= GRID_SIZE:
					coords = [(row+i, col) for i in range(length)]
				else:
					print("Invalid position")
					continue

				if all(board[r][c] == EMPTY for r, c in coords):
					for r, c in coords:
						board[r][c] = SHIP
					ships.append(coords)
					valid = True
				else:
					print("Overlap with another ship")
			except:
				print("Invalid")
	return board, ships

#place computer ships in random spots
def place_computer_ships():
	board = create_board()
	ships = []

	for length in SHIP_LENGTHS:
		placed = False
		while not placed:
			horizontal = random.choice([True, False])
			row = random.randint(0, GRID_SIZE - 1)
			col = random.randint(0, GRID_SIZE - 1)
			coords = []

			if horizontal and col + length <= GRID_SIZE:
				coords = [(row, col+i) for i in range(length)]
			elif not horizontal and row + length <= GRID_SIZE:
				coords = [(row+i, col) for i in range(length)]

			if coords and all(board[r][c] == EMPTY for r, c in coords):
				for r, c in coords:
					board[r][c] = SHIP
				ships.append(coords)
				placed = True
	return board, ships

#get neighboring positions to give to computer
def get_neighbors(row, col):
	neighbors = []
	for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
		r, c = row + dr, col + dc
		if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
			neighbors.append((r,c))
	return neighbors

#computers turn to move
def computer_move(board, moves, targets):
	if targets:
		row, col = targets.pop(0)
		if (row, col) not in moves:
			return computer_move(board, moves, targets)
		moves.remove((row, col))
	else:
		row, col = random.choice(moves)
		moves.remove((row, col))

	print(f"Computer attacks ({row},{string.ascii_uppercase[col]})!")
	if board[row][col] == SHIP:
		board[row][col] = HIT
		print("Computer hit your ship!")
		for n in get_neighbors(row, col):
			if n in moves and n not in targets:
				targets.append(n)
	elif board[row][col] == EMPTY:
		board[row][col] = MISS
		print("Computer missed!")

#are there any ships remaining
def ships_remaining(board):
	for row in board:
		if SHIP in row:
			return True
	return False

#assemble the game
def main():
	print("~~~~~~ BATTLESHIP ~~~~~~")
	player_board, player_ships = place_player_ships()
	computer_board, computer_ships = place_computer_ships()

	moves_left = [(r,c) for r in range(GRID_SIZE) for c in range(GRID_SIZE)]
	target_queue = []

	player_turn = True

	while True:
		print("\nYour Board:")
		print_board(player_board)
		print("Computer's Board:")
		print_board(computer_board, hide_ships=True)

		if not ships_remaining(player_board):
			print("Computer wins!")
			break
		if not ships_remaining(computer_board):
			print("You win!")
			break

		if player_turn:
			valid = False
			while not valid:
				try:
					guess = input("Enter your attack (row col): ")
					parts = guess.split()
					r = int(parts[0])
					c = letter_to_index(parts[1])
					if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
						if computer_board[r][c] in [HIT, MISS]:
							print("Already guessed")
						else:
							if computer_board[r][c] == SHIP:
								computer_board[r][c] = HIT
								print("You hit a ship!")
							else:
								computer_board[r][c] = MISS
								print("You missed!")
							valid = True
					else:
						print("Invalid")
				except:
					print("Invalid")
			player_turn = False
		else:
			computer_move(player_board, moves_left, target_queue)
			player_turn = True

if __name__ == "__main__":
	main()

