import chess.pgn

board = chess.Board()
with open("game.pgn", "r") as file:
    game = chess.pgn.read_game(file)



print(f"White: {game.headers["White"]}")
print(f"Black: {game.headers["Black"]}")
print(f"Result: {game.headers["Result"]}")
print(f"White Elo: {game.headers["WhiteElo"]}")
print(f"Black Elo: {game.headers["BlackElo"]}")

queens_exchanged = False
queen_exchange_move = None
for move in game.mainline_moves():

    board.push(move)
    white_queens = board.pieces(chess.QUEEN, chess.WHITE)
    black_queens = board.pieces(chess.QUEEN, chess.BLACK)

    if len(white_queens) == 0 and len(black_queens) == 0:
        queens_exchanged = True
        queen_exchange_move = board.fullmove_number

print(board)
print(f"Queens exchanged: {queens_exchanged}")
print(queen_exchange_move)
