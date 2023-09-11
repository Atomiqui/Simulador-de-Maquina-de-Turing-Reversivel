from copy import copy

class ReversibleTuringMachine:
    def __init__(self, states, input_symbols, queue_symbols, transitions, entry):
        self.states = states
        self.input_symbols = input_symbols
        self.queue_symbols = queue_symbols

        #Cria as quadruplas
        self.transitions = []
        for transition in transitions:
            self.transitions.extend(transition.to_quadruple())

        #Cria os marcadores
        self.state_marker = transitions[0].current_state
        self.head_marker = 0

        #Cria as fitas
        self.input_tape = entry + "B"
        self.input_tape = list(self.input_tape)
        self.history_tape = []
        self.output_tape = []
        self.final_state = self.transitions[-1].next_state
        
    def make_transitions(self):
        while(self.state_marker != self.final_state):
            nt = 0
            for i in self.transitions:
                if(self.state_marker == i.current_state):
                    if(self.input_tape[self.head_marker] == i.read_symbol):
                        self.state_marker = i.next_state
                        
                        if(i.action == "L"):
                            self.head_marker -= 1
                        elif(i.action == "R"):
                            self.head_marker += 1
                        else:
                            self.input_tape[self.head_marker] = i.action
                            
                        self.history_tape.append(nt) #guarda num transitions
                nt += 1

        self.output_tape = copy(self.input_tape)

    def reverse_movement(self):
        i = len(self.history_tape) - 1
        while i >= 0:
            name = self.history_tape[i]
            if self.transitions[name].action == "R":
                self.head_marker -= 1
            elif self.transitions[name].action == "L":
                self.head_marker += 1
            else:
                self.input_tape[self.head_marker] = self.transitions[name].read_symbol

            i-= 1
            self.history_tape.pop()

    def __str__(self):
        return "Entrada: {}\n Historico: {}\n Output: {}\n".format(self.input_tape, self.history_tape, self.output_tape)
            
