from typing import List, Tuple
from grammar import Grammar

class Parser:

    def __init__(self, grammar: Grammar) -> None:
        self._grammar: Grammar = grammar

    def first(self, not_terminal: str) -> List:

        count_productions: int = 0
        firsts_of_not_terminal: List = []

        not_terminal_productions = self._grammar.lookup_production(not_terminal)

        """Valida si las reglas están en una lista."""
        if isinstance(not_terminal_productions, List):

            production_list: List = []
            state = not_terminal_productions[count_productions]

            if state in self._grammar._terminal:

                production_list.append(state)
                firsts_of_not_terminal.append(production_list)

            elif state in self._grammar._not_terminal:
                
                firsts_of_next_not_termianl = self.first(state)
                reduce_list = [item for sublist in firsts_of_next_not_termianl for item in sublist]

                print(reduce_list)
                if '&' in reduce_list:

                    firsts_of_next_not_termianl = self.first(state)
                    print(firsts_of_next_not_termianl)

                firsts_of_not_terminal.extend(reduce_list)

            else:
                
                firsts_of_not_terminal.append(['&'])

        

        elif isinstance(not_terminal_productions, Tuple):

            for not_terminal_production in not_terminal_productions:

                production_list: List = []

                if isinstance(not_terminal_production, List):

                    state = not_terminal_production[count_productions]

                    if state in self._grammar._terminal:

                        production_list.append(state)
                        firsts_of_not_terminal.append(production_list)

                    elif state in self._grammar._not_terminal:

                        firsts_of_next_not_termianl = self.first(state)
                        reduce_list = [item for sublist in firsts_of_next_not_termianl for item in sublist]
                        print(reduce_list)

                        if '&' in reduce_list:
                            
                            if count_productions >= len(not_terminal_production):

                                firsts_of_not_terminal.append(reduce_list)

                            else:
                                
                                for production in reduce_list:
                                    
                                    print(production)
                                    next_productions: List = []

                                    if '&' != production:

                                        next_productions.append(production)
                                        print(next_productions)
                                        firsts_of_not_terminal.append(next_productions)

                                    else:

                                        state = not_terminal_production[count_productions + 1]
                                        print(state)
                                        firsts_of_next_not_termianl = self.first(state)

                                        if len(firsts_of_next_not_termianl) > 0:
                                            
                                            if '&' in firsts_of_next_not_termianl:

                                                firsts_of_next_not_termianl = self.first(state)

                                            print('aca')
                                            print(firsts_of_next_not_termianl)
                                            reduce_list = [item for sublist in firsts_of_next_not_termianl for item in sublist]
                                            firsts_of_not_terminal.append(reduce_list)

                                        else:
                                            print('aca')
                                            firsts_of_not_terminal.append(reduce_list)
                                            count_productions += 1

                        else:

                            firsts_of_not_terminal.append(reduce_list)
                    
                    else:
                
                        firsts_of_not_terminal.append(['&'])

        else:

            firsts_of_not_terminal.append(['&'])
        
        return firsts_of_not_terminal

    def _peek_token(self) -> str:
        if self._read_position >= len(self._source):
            return ''
        
        return self._source[self._read_position]

    def see_grammar(self) -> None:
        print(self._grammar)