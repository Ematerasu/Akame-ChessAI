from chess import ROOK


PAWN_VALUE = 1
KNIGHT_VALUE = 3
BISHOP_VALUE = 3
ROOK_VALUE = 5
QUEEN_VALUE = 9
KING_VALUE = 100

GET_VALUE = {
            'p' : PAWN_VALUE,
            'n' : KNIGHT_VALUE,
            'b' : BISHOP_VALUE,
            'r' : ROOK_VALUE,
            'q' : QUEEN_VALUE,
            'k' : KING_VALUE,
            'P' : -PAWN_VALUE,
            'N' : -KNIGHT_VALUE,
            'B' : -BISHOP_VALUE,
            'R' : -ROOK_VALUE,
            'Q' : -QUEEN_VALUE,
            'K' : -KING_VALUE
        }
