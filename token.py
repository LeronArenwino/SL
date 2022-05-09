from enum import(
  auto,
  Enum,
  unique
)
from typing import (
  NamedTuple,
  Dict,
)

@unique
class TokenType(Enum):
  # Operators and special symbols
  TK_ASIGNACION = auto() # One '='
  TK_COMA = auto() # One ','
  TK_CORCHETE_DERECHO = auto() # One ']'
  TK_CORCHETE_IZQUIERDO = auto() # One '['  
  TK_DIVISION = auto() # One '/'
  TK_DOS_PUNTOS = auto() # One ':'
  TK_LLAVE_DERECHA = auto() # One '}'
  TK_LLAVE_IZQUIERDA = auto() # One '{'
  TK_MAYOR = auto() # One '>'
  TK_MENOR = auto() # One '<'W
  TK_MODULO = auto() # One '%'
  TK_MULTIPLICACION = auto() # One '*'
  TK_PARENTESIS_DERECHO = auto() # One ')'
  TK_PARENTESIS_IZQUIERDO = auto() # One '('
  TK_POTENCIACION = auto() # One '^'
  TK_PUNTO = auto() # One '.'
  TK_PUNTO_Y_COMA = auto() # One ';'
  TK_RESTA = auto() # One '-'
  TK_SUMA = auto() # One '+'

  # Two operators
  TK_DISTINTO_DE = auto() # Two '<>'
  TK_IGUAL_QUE = auto() # Two '=='
  TK_MAYOR_IGUAL = auto() # Two'>='
  TK_MENOR_IGUAL = auto() # Two '<='

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
    if self.literal == 'SI':
      return f'<{self.token_type.name},{self.literal},{self.lineno},{self.position}>'
    else:
      return f'<{self.token_type.name.lower()},{self.literal},{self.lineno},{self.position}>'

def lookup_token_type(literal: str) -> TokenType:
  keywords: Dict[str, TokenType] = {

    # Reserved
    'and': TokenType.AND,
    'constantes': TokenType.CONSTANTES,
    'hasta': TokenType.HASTA,
    'matriz': TokenType.MATRIZ,
    'paso': TokenType.PASO,
    'registro': TokenType.REGISTRO,
    'sino': TokenType.SINO,
    'vector': TokenType.VECTOR,
    'archivo': TokenType.ARCHIVO,
    'desde': TokenType.DESDE,
    'inicio': TokenType.INICIO,
    'mientras': TokenType.MIENTRAS,
    'subrutina': TokenType.SUBRUTINA,
    'repetir': TokenType.REPETIR,
    'tipos': TokenType.TIPOS,
    'caso': TokenType.CASO,
    'eval': TokenType.EVAL,
    'lib': TokenType.LIB,
    'not': TokenType.NOT,
    'programa': TokenType.PROGRAMA,
    'retorna': TokenType.RETORNA,
    'var': TokenType.VAR,
    'const': TokenType.CONST,
    'fin': TokenType.FIN,
    'libext': TokenType.LIBEXT,
    'or': TokenType.OR,
    'ref': TokenType.REF,
    'si': TokenType.si,
    'variables': TokenType.VARIABLES,

    # Data types
    'numerico': TokenType.NUMERICO,
    'tk_numero': TokenType.TK_NUMERO,
    'logico': TokenType.LOGICO,
    'tk_logico': TokenType.TK_LOGICO,
    'cadena': TokenType.CADENA,
    'tk_cadena': TokenType.TK_CADENA,
    'true': TokenType.TRUE,
    'false': TokenType.TRUE,
    'SI': TokenType.SI,
    'NO': TokenType.NO,

    # Functions
    'leer': TokenType.LEER,
    'imprimir': TokenType.IMPRIMIR,
    'dim': TokenType.DIM,
    'cls': TokenType.CLS,
    'set_ifs': TokenType.SET_IFS,
    'abs': TokenType.ABS,
    'arctan': TokenType.ARCTAN,
    'ascii': TokenType.ASCII,
    'cos': TokenType.COS,
    'dec': TokenType.DEC,
    'eof': TokenType.EOF,
    'exp': TokenType.EXP,
    'get_ifs': TokenType.GET_IFS,
    'inc': TokenType.INC,
    'int': TokenType.INT,
    'log': TokenType.LOG,
    'lower': TokenType.LOWER,
    'mem': TokenType.MEM,
    'ord': TokenType.ORD,
    'paramval': TokenType.PARAMVAL,
    'pcount': TokenType.PCOUNT,
    'pos': TokenType.POS,
    'random': TokenType.RANDOM,
    'sec': TokenType.SEC,
    'set_stdin': TokenType.SET_STDIN,
    'set_stdout': TokenType.SET_STDOUT,
    'sin': TokenType.SIN,
    'sqrt': TokenType.SQRT,
    'str': TokenType.STR,
    'strdup': TokenType.STRDUP,
    'strlen': TokenType.STRLEN,
    'substr': TokenType.SUBSTR,
    'tan': TokenType.TAN,
    'upper': TokenType.UPPER,
    'val': TokenType.VAL,
    'alen': TokenType.ALEN,

  }

  return keywords.get(literal, TokenType.ID)