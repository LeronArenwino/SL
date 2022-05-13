from typing import List
from grammar import Grammar

class Parser:

    def __init__(self, grammar: Grammar) -> None:
        self._grammar: Grammar = grammar

    def see_grammar(self) -> None:
        print(self._grammar)