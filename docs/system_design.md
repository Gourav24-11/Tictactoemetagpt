## Implementation approach:
For the tic tac toe game, we will use the pygame library to create the game interface and handle user input. We will implement the game logic using a simple class-based approach. To provide intelligent AI for single-player mode, we will use the minimax algorithm. 

## Python package name:
```python
"tic_tac_toe_game"
```

## File list:
```python
[
    "main.py",
    "game.py",
    "board.py",
    "player.py",
    "ai.py"
]
```

## Data structures and interface definitions:
```mermaid
classDiagram
    class Game{
        +start_game()
        +restart_game()
        +get_current_state() : str
        +get_winner() : Optional[str]
        +get_current_player() : str
        +make_move(row: int, col: int) : bool
    }

    class Board{
        +__init__(size: int)
        +get_size() : int
        +get_cell(row: int, col: int) : Optional[str]
        +set_cell(row: int, col: int, symbol: str) : bool
        +is_full() : bool
        +is_winner(symbol: str) : bool
    }

    class Player{
        +__init__(symbol: str)
        +get_symbol() : str
    }

    class AI{
        +__init__(symbol: str)
        +get_symbol() : str
        +get_best_move(board: Board) : Tuple[int, int]
    }

    Game "1" -- "1" Board: has
    Game "1" -- "2" Player: has
    Game "1" -- "2" AI: has
    Board "1" -- "many" Cell: contains
```

## Program call flow:
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant B as Board
    participant P1 as Player1
    participant P2 as Player2
    participant A as AI

    M->>G: start_game()
    G->>B: __init__(size)
    G->>P1: __init__(symbol)
    G->>P2: __init__(symbol)
    G->>A: __init__(symbol)
    G->>M: get_current_state()
    M->>G: make_move(row, col)
    G->>B: set_cell(row, col, symbol)
    G->>B: is_full()
    G->>B: is_winner(symbol)
    G->>A: get_best_move(board)
    G->>M: get_current_state()
    G->>M: get_winner()
    G->>M: get_current_player()
    G->>M: restart_game()
```

## Anything UNCLEAR:
The requirement is clear to me.