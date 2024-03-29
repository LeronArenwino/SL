from grammar import Grammar
from lexer import Lexer
from token import Token
from typing import (
    Dict,
    List,
    Set,
    Tuple
)
from re import (
    match,
    search,
)

from parser import Parser

def _comment_list(sources: str) -> List:
    
    comment_list: List[Tuple] = []
    right_list: List[Tuple] = []
    pos_comment: bool = False
    
    for line, source in enumerate(sources):
        for pos in range(len(source)-1):
            if bool(match(r'\/', source[pos])) and bool(match(r'\*', source[pos+1])) and not pos_comment:
                pos_comment = True
                right_list.append((pos, line))
                pos += 1
            elif bool(match(r'\*', source[pos])) and bool(match(r'\/', source[pos + 1])) and pos_comment:
                pos_comment = False
                aux_tuple = tuple(right_list[0])
                comment_list.append((aux_tuple[0], aux_tuple[1] + 1, pos + 1, line + 1))
                right_list.clear()
    
    return comment_list

def _tokens_generator(sources: str, comment_list: List) -> List:
    
    comment: bool = False
    check_status: bool = True
    token_list: List[Token] = []

    for line, source in enumerate(sources):

        tmp_tokens: List[Token] = []

        lexer: Lexer = Lexer(source, line + 1, comment, comment_list)

        for i in range(len(source)):
            token = lexer.next_token()
            if check_status and token != None:
                tmp_tokens.append(token)
                if token.token_type.name == 'TK_ILEGAL':
                    check_status = False
                    break

        comment = getattr(lexer, '_is_comment')

        token_list.extend(tmp_tokens) 

    return token_list

def start_repl() -> None:
    
    eof_if: bool = True
    sources: List = []

    while eof_if:
        try:
            source = input()
            if bool(search(r'^\!$', source)):
                eof_if = False
        except EOFError:
            break
        sources.append(source)

    comment_list: List = _comment_list(sources)

    tokens: List = _tokens_generator(sources, comment_list)

    # for token in tokens:
    #     print(token)

    not_terminal: List = ['A', 'B', 'C', 'D']
    terminal: List = ['bet','bad', 'big', 'boss', 'cat', 'cow', 'dat', 'bat']
    initial_symbol: str = 'A'
    productions: Dict[str, List] = {
        'A': [['B', 'C'], ['bad']],
        'B': [['big', 'C', 'boss'], ['&']],
        'C': [['cat'], ['cow']],
    }

    grammar: Grammar = Grammar(not_terminal, terminal, initial_symbol, productions)

    parser: Parser = Parser(grammar)

    first_of_A = parser.firsts_of_not_terminal('A')
    print(first_of_A)
    first_of_B = parser.firsts_of_not_terminal('B')
    print(first_of_B)
    first_of_C = parser.firsts_of_not_terminal('C')
    print(first_of_C)

    # after_of_A = parser.afters_of_not_terminal('A')
    # print(after_of_A)