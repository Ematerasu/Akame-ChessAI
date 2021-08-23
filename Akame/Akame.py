import chess
import random

class Akame():
    def __init__(self) -> None:
        self.name = "Akame"
        self.board = chess.Board()
    
    def move(self, board: chess.Board()) -> chess.Move:
        self.board = board
        legal_moves = list(self.board.legal_moves)
        return legal_moves[random.randint(0, len(legal_moves)-1)]

    def evaluate(self):
        pass