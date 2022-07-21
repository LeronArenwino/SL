from typing import List, Tuple
from grammar import Grammar

class Parser:

    def __init__(self, grammar: Grammar) -> None:
        self._grammar: Grammar = grammar

    def firsts_of_not_terminal(self, not_terminal: str) -> List:

        firsts_of_not_terminal: List = []
        count_state: int = 0

        not_terminal_rules = self._grammar.lookup_production(not_terminal)

        for not_terminal_rule in not_terminal_rules:

            # Valida si el único elemento de la regla para el no terminal es epsilon
            if len(not_terminal_rules) == 1 and len(not_terminal_rule) == 1 and not_terminal_rule[0] == '&':
                
                firsts_of_not_terminal.append('&')
                
                return firsts_of_not_terminal
            
            if len(not_terminal_rule) == 1 and not_terminal_rule[0] == '&':
                
                firsts_of_not_terminal.append('&')
                
                return firsts_of_not_terminal

            state = not_terminal_rule[count_state]

            if state in self._grammar._terminal:

                firsts_of_not_terminal.append(state)
            
            elif state in self._grammar._not_terminal:

                next_firsts_of_not_terminal = self.firsts_of_not_terminal(state)
                if '&' in next_firsts_of_not_terminal:
                    next_firsts_of_not_terminal.remove('&')

                epsilon_in_not_terminal: bool = False

                next_not_terminal_rules = self._grammar.lookup_production(state)

                for next_not_terminal_rule in next_not_terminal_rules:

                    if '&' in next_not_terminal_rule:

                        epsilon_in_not_terminal = True
                        break

                if epsilon_in_not_terminal:
                    
                    if len(next_not_terminal_rules) == 1:

                        firsts_of_not_terminal.append('&')
                    
                    else:
                        if count_state >= len(not_terminal_rule) - 1:
                            pass
                        else:
                            state = not_terminal_rule[count_state + 1]

                            next_firsts_of_not_terminal.extend(self.firsts_of_not_terminal(state))

                firsts_of_not_terminal.extend(next_firsts_of_not_terminal)

        return firsts_of_not_terminal

    def _peek_token(self) -> str:
        if self._read_position >= len(self._source):
            return ''
        
        return self._source[self._read_position]

    def see_grammar(self) -> None:
        print(self._grammar)