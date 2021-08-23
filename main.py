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
        board.push(akame.move(board))
    print(board.result())