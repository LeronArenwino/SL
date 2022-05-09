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

        self._skip_whitespace()

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
        elif self._is_letter(self._character):
            
            initial_position = self._position + 1
            literal = self._read_identifier()
            token_type = lookup_token_type(literal)

            return Token(token_type, literal, self._line, initial_position)
        elif self._is_number(self._character):

            initial_position = self._position + 1
            literal = self._read_number()

            return Token(TokenType.TK_NUMERO, literal, self._line, initial_position)
        else:
            if len(self._character) >= 1:
                token = Token(TokenType.TK_ILEGAL, self._character, self._line, self._position + 1)
            else:
                return None

        self._read_character()

        return token
    
    def _is_exp(self, character: str) -> bool:
        """Valida si el carácter es un 'E' o 'e'."""
        return bool(match(r'[Ee]+', character))

    def _is_letter(self, character: str) -> bool:
        """Valida si el carácter es una letra permitida."""
        return bool(match(r'[a-zA-ZñÑ_][a-zA-ZñÑ0-9_]*', character))

    def _is_number(self, character: str) -> bool:
        """Valida si el carácter es un número."""
        return bool(match(r'\d+',character))

    # Valida si es punto decimal
    def _is_point(self, character:str) -> bool:
        """Valida si el carácter es un punto."""
        return bool(match(r'[.]', character))

    def _is_symbol(self, character: str) -> bool:
        """Valida si el carácter es un signo '-' o '+'."""
        return bool(match(r'[-+]', character))

    def _read_character(self) -> None:
        """Lee el siguiente carácter de la cadena."""
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1

    def _read_identifier(self) -> str:
        """Lee la secuencia de carácteres."""
        initial_position = self._position

        while self._is_letter(self._character):
            self._read_character()

        return self._source[initial_position:self._position]
    
    def _read_number(self) -> str:
        """Lee la secuencia de carácteres númericos."""
        initial_position = self._position

        while self._is_number(self._character):
            self._read_character()

        while self._is_point(self._character):
            self._read_character()
        
        while self._is_number(self._character):
            self._read_character()

        while self._is_exp(self._character):
            self._read_character()

        while self._is_symbol(self._character):
            self._read_character()

        while self._is_number(self._character):
            self._read_character()

        return self._source[initial_position:self._position]

    def _skip_whitespace(self) -> None:
        """Permite leer el siguiente carácter cuando lee un espacio en blanco."""
        while match(r'^\s$', self._character):
            self._read_character()