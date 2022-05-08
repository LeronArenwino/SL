from lexer import Lexer
from token import Token
from typing import (
    List,
    Tuple
)
from re import (
    match,
    search,
)

comment: bool = False
sources = []
check_status: bool = True
eof_if: bool = True
pos_comment: bool = False
right_list: List[Tuple] = []
comment_list: List[Tuple] = []

while check_status and eof_if:
    try:
        line = input()
        if bool(search(r'^\!$', line)):
            eof_if = False
    except EOFError:
        break
    sources.append(line)

for line, source in enumerate(sources):

    tokens: List[Token] = []
    lexer: Lexer = Lexer(source, line + 1)

    for i in range(len(source)):
        token = lexer.next_token()
        if token != None:
            if check_status:
                tokens.append(token)
                # token_list.append(token)
                # if token.token_type == 'tk_ilegal':
                #     check_status = False
                #     break

    # comment = getattr(lexer, '_comment') 

    for token in tokens:
        print(token)
