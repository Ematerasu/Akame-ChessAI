# Akame-ChessEngine
Simple chess engine that I use as a learning experience in the AI world

## Tools used
I use python chess module to simulate game of chess.
You can find it here -> https://python-chess.readthedocs.io/en/latest/index.html

## Current level of strenght
Around 1100 elo, makes not bad moves, evaluates to depth of 3.

- Early game - Akame doesn't know any game theory. Right now She makes simple evaluation based on piece's value and it's position.
- Mid game - Pretty good moves, tries to get king in check, makes some good cheesy moves.
- End game - Prefers to suffocate enemy by taking all his pieces and then checkmates, it's most likely because of depth, it is too shallow to fast mate in endgame. Because of that we might end up in situation where Akame needs to push the pawn to promote but it requires 5 pawn moves, so Akame can't win the game.

Bots on chess.com that Akame has beaten:
- Jimmy (600 elo)
- Martin (250 elo)
- Elani (400 elo)
- Aron (700 elo)
- Emir (1000 elo)

## How to play
Right now the only way to play the game with Akame is through terminal. Clone repository and run main.py, then board will pop-up with list of legal moves (it's helpful because you need to correctly input your move in san). Just input your move and wait for Akame's response.

## TODO
- Make the code much more cleaner
- Recognize weakness of doubled pawns
- Recognize advantage of castling
- Increase depth without losing so much performance
