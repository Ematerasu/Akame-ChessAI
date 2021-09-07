# Akame-ChessEngine
Simple chess engine that I use as a learning expierience in the AI world

## Tools used
I use python chess module to simulate game of chess.
You can find it here -> https://python-chess.readthedocs.io/en/latest/index.html

## Current level of strenght
Around 600 elo, makes not bad moves, evaluates to depth of 3.
Early game - Akame doesn't know any game theory. Right now She makes simple evaluation based on piece's value and it's position.
Mid game - Pretty good moves, tries to get king in check, makes some good cheesy moves.
End game - can't check mate, usually keeps enemy's king in check till repetition occurs and game end :(.

## How to play
Right now the only way to play the game with Akame is through terminal. Clone repository and run main.py, then board will pop-up with list of legal moves (it's helpful because you need to correctly input your move in san). Just input your move and wait for Akame's response.
