import chess
from .pieceValues import *
from .heatmaps import *

class Akame():
    def __init__(self) -> None:
        self.name = "Akame"
        self.board = chess.Board()
        self.color = "b"
    
    def move(self, board: chess.Board) -> chess.Move:
        self.board = board
        currentSituation = self.evaluate(self.board)
        print(currentSituation)
        best_move = self.minmaxRoot(3, -9999, 9999)
        return best_move

    def evaluate(self, board: chess.Board) -> float:
        eval = 0
        boardFen = board.fen()
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
                    piece_value = GET_VALUE[letter]+GET_MAP[letter][i][j]
                    eval += piece_value if letter.isupper() else -piece_value
                    j+=1
        return eval

    def minmaxRoot(self, depth: int, alpha: int, beta: int) -> int:
        legal_moves = list(self.board.legal_moves)
        best = alpha
        best_move = None
        for move in legal_moves:

            self.board.push(move)
            new = self.minmaxNode(depth-1, alpha, beta, False)
            self.board.pop()
            #print(f"\t{move}, {new}: ")
            if new > best:
                best = new
                best_move = move
        return best_move


    def minmaxNode(self, depth: int, alpha: int, beta: int, myMove: bool) -> int:
        if depth == 0:
            return -self.evaluate(self.board)
        
        legal_moves = list(self.board.legal_moves)

        if myMove:
            best = -9999

            for move in legal_moves:

                self.board.push(move)
                new = self.minmaxNode(depth-1, alpha, beta, not myMove)
                self.board.pop()

                if new > best:
                    best = new
                
                alpha = max(alpha, best)

                if beta <= alpha:
                    return best
            return best
        else:
            best = 9999

            for move in legal_moves:

                self.board.push(move)
                new = self.minmaxNode(depth-1, alpha, beta, not myMove)
                self.board.pop()

                if new < best:
                    best = new
                    
                beta = min(beta, best)

                if beta <= alpha:
                    return best
            return best
                

    
    