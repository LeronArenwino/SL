from typing import (
    Dict,
    List,
    Tuple
)

class Grammar:

    def __init__(self, not_terminal: List, terminal: List, initial_symbol: str, productions: Dict[str, Tuple]) -> None:
        self._not_terminal: List = not_terminal
        self._terminal: List = terminal
        self._initial_symbol: str = initial_symbol
        self._productions: Dict[str, Tuple] = productions

    def __str__(self) -> str:
        return f'grammar: {self._not_terminal}, {self._terminal}, {self._initial_symbol}, {self._productions}'