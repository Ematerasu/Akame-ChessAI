from Akame.heatmaps import GET_MAP
import chess

PAWN_VALUE = 10
KNIGHT_VALUE = 30
BISHOP_VALUE = 30
ROOK_VALUE = 50
QUEEN_VALUE = 90
KING_VALUE = 500

GET_VALUE = {
            'p' : PAWN_VALUE,
            'n' : KNIGHT_VALUE,
            'b' : BISHOP_VALUE,
            'r' : ROOK_VALUE,
            'q' : QUEEN_VALUE,
            'k' : KING_VALUE,
            'P' : PAWN_VALUE,
            'N' : KNIGHT_VALUE,
            'B' : BISHOP_VALUE,
            'R' : ROOK_VALUE,
            'Q' : QUEEN_VALUE,
            'K' : KING_VALUE
        }

def get_piece_value(piece: chr, board: chess.Board, pos: tuple) -> float:
    value = 0.0
    value += GET_VALUE[piece] + GET_MAP[piece][pos[0]][pos[1]]
    """
    temp = list(board.attacks(pos[0]*8+pos[1]))
    for elem in temp:
        x = board.piece_at(elem)
        if x is not None:
            if (x.color and piece.isupper()) or (not x.color and piece.islower()):
                value += GET_VALUE[x.symbol()]*0.5

    """
    return value
