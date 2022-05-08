from enum import(
  auto,
  Enum,
  unique
)
from typing import NamedTuple

@unique
class TokenType(Enum):
  # Operators and special symbols
  TK_ASIGNACION = auto()
  TK_COMA = auto()
  TK_CORCHETE_DERECHO = auto()
  TK_CORCHETE_IZQUIERDO = auto()
  TK_DISTINTO_DE = auto()
  TK_DIVISION = auto()
  TK_DOS_PUNTOS = auto()
  TK_IGUAL_QUE = auto()
  TK_LLAVE_DERECHA = auto()
  TK_LLAVE_IZQUIERDA = auto()
  TK_MAYOR = auto()
  TK_MAYOR_IGUAL = auto()
  TK_MENOR = auto()
  TK_MENOR_IGUAL = auto()
  TK_MODULO = auto()
  TK_MULTIPLICACION = auto()
  TK_PARENTESIS_DERECHO = auto()
  TK_PARENTESIS_IZQUIERDO = auto()
  TK_POTENCIACION = auto()
  TK_PUNTO = auto()
  TK_PUNTO_Y_COMA = auto()
  TK_RESTA = auto()
  TK_SUMA = auto()

  # Reserved
  AND = auto()
  CONSTANTES = auto()
  HASTA = auto()
  MATRIZ = auto()
  PASO = auto()
  REGISTRO = auto()
  SINO = auto()
  VECTOR = auto()
  ARCHIVO = auto()
  DESDE = auto()
  INICIO = auto()
  MIENTRAS = auto()
  SUBRUTINA = auto()
  REPETIR = auto()
  TIPOS = auto()
  CASO = auto()
  EVAL = auto()
  LIB = auto()
  NOT = auto()
  PROGRAMA = auto()
  RETORNA = auto()
  VAR = auto()
  CONST = auto()
  FIN = auto()
  LIBEXT = auto()
  OR = auto()
  REF = auto()
  si = auto()
  VARIABLES = auto()

  # Data types
  NUMERICO = auto()
  TK_NUMERO = auto()
  LOGICO = auto()
  TK_LOGICO = auto()
  CADENA = auto()
  TK_CADENA = auto()
  TRUE = auto()
  FALSE = auto()
  SI = auto()
  NO = auto()

  # Functions
  LEER = auto()
  IMPRIMIR = auto()
  DIM = auto()
  CLS = auto()
  SET_IFS = auto()
  ABS = auto()
  ARCTAN = auto()
  ASCII = auto()
  COS = auto()
  DEC = auto()
  EOF = auto()
  EXP = auto()
  GET_IFS = auto()
  INC = auto()
  INT = auto()
  LOG = auto()
  LOWER = auto()
  MEM = auto()
  ORD = auto()
  PARAMVAL = auto()
  PCOUNT = auto()
  POS = auto()
  RANDOM = auto()
  SEC = auto()
  SET_STDIN = auto()
  SET_STDOUT = auto()
  SIN = auto()
  SQRT = auto()
  STR = auto()
  STRDUP = auto()
  STRLEN = auto()
  SUBSTR = auto()
  TAN = auto()
  UPPER = auto()
  VAL = auto()
  ALEN = auto()

  # Extra
  ID = auto()
  TK_ILEGAL = auto()

class Token(NamedTuple):
  token_type: TokenType
  literal: str
  lineno: int
  position: int

  def __str__(self) -> str:
    return f'<{self.token_type.name.lower()},{self.literal},{self.lineno},{self.position}>'