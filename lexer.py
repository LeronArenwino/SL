from token import (
    Token,
    TokenType
)
from re import match

class Lexer:

    def __init__(self, source: str, line: int) -> None:
        self._source: str = source
        self._line: int = line
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0

        self._read_character()

    def next_token(self) -> Token:
        if match(r'\=', self._character):
            token = Token(TokenType.TK_ASIGNACION, self._character, self._line, self._position + 1)
        elif match(r'\+', self._character):
            token = Token(TokenType.TK_SUMA, self._character, self._line, self._position + 1)
        else:
            token = Token(TokenType.TK_ILEGAL, self._character, self._line, self._position + 1)

        self._read_character()

        return token
    
    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1
    