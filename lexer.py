from token import (
    lookup_token_type,
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
        elif match(r'\,', self._character):
            token = Token(TokenType.TK_COMA, self._character, self._line, self._position + 1)
        elif match(r'\]', self._character):
            token = Token(TokenType.TK_CORCHETE_DERECHO, self._character, self._line, self._position + 1)
        elif match(r'\[', self._character):
            token = Token(TokenType.TK_CORCHETE_IZQUIERDO, self._character, self._line, self._position + 1)
        elif match(r'\/', self._character):
            token = Token(TokenType.TK_DIVISION, self._character, self._line, self._position + 1)
        elif match(r'\:', self._character):
            token = Token(TokenType.TK_DOS_PUNTOS, self._character, self._line, self._position + 1)
        elif match(r'\}', self._character):
            token = Token(TokenType.TK_LLAVE_DERECHA, self._character, self._line, self._position + 1)
        elif match(r'\{', self._character):
            token = Token(TokenType.TK_LLAVE_IZQUIERDA, self._character, self._line, self._position + 1)
        elif match(r'\>', self._character):
            token = Token(TokenType.TK_MAYOR, self._character, self._line, self._position + 1)
        elif match(r'\<', self._character):
            token = Token(TokenType.TK_MENOR, self._character, self._line, self._position + 1)
        elif match(r'\%', self._character):
            token = Token(TokenType.TK_MODULO, self._character, self._line, self._position + 1)
        elif match(r'\*', self._character):
            token = Token(TokenType.TK_MULTIPLICACION, self._character, self._line, self._position + 1)
        elif match(r'\)', self._character):
            token = Token(TokenType.TK_PARENTESIS_DERECHO, self._character, self._line, self._position + 1)
        elif match(r'\(', self._character):
            token = Token(TokenType.TK_PARENTESIS_IZQUIERDO, self._character, self._line, self._position + 1)
        elif match(r'\^', self._character):
            token = Token(TokenType.TK_POTENCIACION, self._character, self._line, self._position + 1)
        elif match(r'\.', self._character):
            token = Token(TokenType.TK_PUNTO, self._character, self._line, self._position + 1)
        elif match(r'\;', self._character):
            token = Token(TokenType.TK_PUNTO_Y_COMA, self._character, self._line, self._position + 1)
        elif match(r'\-', self._character):
            token = Token(TokenType.TK_RESTA, self._character, self._line, self._position + 1)
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
    