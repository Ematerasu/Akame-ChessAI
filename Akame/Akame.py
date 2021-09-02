import chess
from .pieceValues import *
from .heatmaps import *

class Akame():
    def __init__(self) -> None:
        self.name = "Akame"
        self.board = chess.Board()
        self.color = "b"
    
    def move(self, board: chess.Board()) -> chess.Move:
        self.board = board
        legal_moves = list(self.board.legal_moves)
        currentSituation = self.evaluate()
        if self.color == "b":
            currentSituation *= -1
        
        print(currentSituation)
        return legal_moves[0]

    def evaluate(self) -> float:
        eval = 0
        boardFen = self.board.fen()
        i, j = 0, 0
        for index, letter in enumerate(boardFen):
            if letter == ' ':
                break
            if letter == '/':
                i += 1
                j = 0
            else:
                if letter.isdigit():
                    j += ord(letter) - 48
                else:
                    eval += GET_VALUE[letter]*GET_MAP[letter][i][j]
                    j+=1
        return eval

    def minmaxroot(self, depth, alpha, beta, board):
        pass
                

    
    