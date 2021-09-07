from Akame import Akame
import chess

if __name__ == "__main__":
    akame = Akame.Akame()
    board = chess.Board()
    while not board.is_game_over():
        print(board.legal_moves)
        print(board)
        move = board.parse_san(input())
        if move in board.legal_moves:
            board.push(move)
        else:
            print("Illegal move!")
        if board.is_game_over():
            break
        akame_move = akame.move(board)
        print(f"Akame's move: {akame_move}")
        board.push(akame_move)
    print(board.result())