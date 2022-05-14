from typing import List, Tuple
from grammar import Grammar

class Parser:

    def __init__(self, grammar: Grammar) -> None:
        self._grammar: Grammar = grammar

    def first(self, not_terminal: str) -> Tuple:

        firsts_of_not_terminal: List = []

        not_terminal_productions = self._grammar.lookup_production(not_terminal)

        if isinstance(not_terminal_productions, List):

            state = not_terminal_productions[0]

            if state in self._grammar._terminal:

                firsts_of_not_terminal.append(state)

            elif state in self._grammar._not_terminal:

                firsts_of_next_not_termianl = self.first(state)
                firsts_of_not_terminal.extend(firsts_of_next_not_termianl)

            else:
                
                firsts_of_not_terminal.append('&')

        elif isinstance(not_terminal_productions, Tuple):

            for not_terminal_production in not_terminal_productions:

                production_list: List = []

                if isinstance(not_terminal_production, List):

                    state = not_terminal_production[0]

                    if state in self._grammar._terminal:

                        production_list.append(state)
                        firsts_of_not_terminal.append(production_list)

                    elif state in self._grammar._not_terminal:

                        firsts_of_next_not_termianl = self.first(state)
                        reduce_list = [item for sublist in firsts_of_next_not_termianl for item in sublist]
                        firsts_of_not_terminal.append(reduce_list)
                    
                    else:
                
                        firsts_of_not_terminal.append('&')

        else:

            firsts_of_not_terminal.append('&')
        
        return tuple(firsts_of_not_terminal)

    def see_grammar(self) -> None:
        print(self._grammar)