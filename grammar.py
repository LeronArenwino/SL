from typing import (
    Dict,
    Set
)

class Grammar:

    def __init__(self, not_terminal: Set, terminal: Set, initial_symbol: str, productions: Dict) -> None:
        self._not_terminal: Set = not_terminal
        self._terminal: Set = terminal
        self._initial_symbol: str = initial_symbol
        self._productions: Dict = productions

    def __str__(self) -> str:
        return f'grammar: {self._not_terminal}, {self._terminal}, {self._initial_symbol}, {self._productions}'