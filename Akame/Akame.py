import chess
from .pieceValues import *
from .heatmaps import *

class Akame():
    def __init__(self, isWhite: bool) -> None:
        self.name = "Akame"
        self.board = chess.Board()
        self.color = isWhite
    
    def move(self, board: chess.Board, depth: int) -> chess.Move:
        self.board = board
        currentSituation = self.evaluate(self.board)
        print(currentSituation)
        move_counter = len(self.board.move_stack)
        depth += move_counter // 60
        best_move = self.minmaxRoot(depth, -9999, 9999)
        return best_move

    def akame_won(self) -> bool:
        if self.board.is_game_over():
            if self.board.outcome().winner == self.color:
                return True
            else:
                return False
        return False

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
            if new > best:
                best = new
                best_move = move
        return best_move


    def minmaxNode(self, depth: int, alpha: int, beta: int, myMove: bool) -> int:
        if self.board.is_game_over():
            if self.board.is_checkmate():
                if self.akame_won():
                    return 99999
                else:
                    return -99999
            elif self.board.is_repetition():    
                #Draw is bad for us if we're winning and good for us if we are losing so we just return negative evaluation
                if self.color:
                    return -self.evaluate(self.board)
                else:
                    return self.evaluate(self.board)
            elif self.board.is_stalemate():
                if self.color:
                    return -self.evaluate(self.board)
                else:
                    return self.evaluate(self.board)

        
        if depth == 0:
            if self.color:
                return self.evaluate(self.board)
            else:
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
                

    
    