from typing import List
from grammar import Grammar

class Parser:

    def __init__(self, grammar: Grammar) -> None:
        self._grammar: Grammar = grammar

    def first(self, not_terminal: str) -> None:
        print(self._grammar.lookup_production(not_terminal))
        not_terminal_productions = self._grammar.lookup_production(not_terminal)

        if isinstance(not_terminal_productions, List):
            print(not_terminal_productions[0])
        else:
            for not_terminal_production in not_terminal_productions:
                if isinstance(not_terminal_production, List):
                    print(not_terminal_production[0])  

    def see_grammar(self) -> None:
        print(self._grammar)