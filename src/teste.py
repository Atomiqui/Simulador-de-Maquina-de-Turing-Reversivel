import sys
from copy import copy

class Quadruple:
    def __init__(self, current_state, read_symbol, next_state, action):
        self.current_state = current_state
        self.read_symbol = read_symbol
        self.next_state = next_state
        self.action = action

    def __str__(self):
        return "({},{})=({},{})".format(self.current_state, self.read_symbol, self.next_state, self.action)

class Quintuple:
    def __init__(self, transition):
        self.current_state, self.read_symbol = transition[transition.index("(") + 1:transition.index(")")].split(",")
        transition = transition[transition.index("=") + 1:]

        self.next_state, self.write_symbol, self.head_movement = transition[transition.index("(") + 1:transition.index(")")].split(",")

        self.current_state = self.current_state
        self.next_state = self.next_state

    def to_quadruple(self):
        q1 = Quadruple(self.current_state, self.read_symbol, self.next_state + "*", self.write_symbol)
        q2 = Quadruple(self.next_state + "*", self.write_symbol, self.next_state, self.head_movement)
        return [q1,q2]

    def __str__(self):
        return "({},{})=({},{},{})".format(self.current_state, self.read_symbol, self.next_state, self.write_symbol, self.head_movement)

class ReversibleTuringMachine:
    def __init__(self, states, input_symbols, queue_symbols, transitions, entry):
        self.states = states
        self.input_symbols = input_symbols
        self.queue_symbols = queue_symbols

        # Cria as quadruplas
        self.transitions = []
        for transition in transitions:
            self.transitions.extend(transition.to_quadruple())

        # Cria os marcadores
        self.state_marker = transitions[0].current_state
        self.head_marker = 0

        # Cria as fitas
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

# Para rodar no windows:
# Comente as próximas duas linhas e
file = sys.stdin
content = file.readlines()

# descomente as próximas duas linhas.
# with open('entrada-quintupla.txt', 'r') as file:
#     content = file.readlines()

num_states, num_input_symbols, num_queue_symbols, num_transitions = content[0].split()
str_states = content[1].split()

input_symbols = content[2].split()
queue_symbols = content[3].split()
transitions = []

for i in range(4, 4 + int(num_transitions)):
    transitions.append(Quintuple(content[i]))

entry = content[-1]

print("MT Lida:\n")
print(num_states + " " + num_input_symbols + " " + num_queue_symbols + " " + num_transitions)
print(' '.join(str_states))
print(' '.join(input_symbols))
print(' '.join(queue_symbols))
# print(' '.join(str_states))
for transition in transitions:
    print(transition)

reversibleTuringMachine = ReversibleTuringMachine(num_states, input_symbols, queue_symbols, transitions, entry)

reversibleTuringMachine.make_transitions()

print(reversibleTuringMachine)

reversibleTuringMachine.reverse_movement()

print(reversibleTuringMachine)