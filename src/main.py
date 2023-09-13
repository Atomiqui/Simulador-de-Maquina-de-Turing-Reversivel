# Grupo:
# Alisson

import sys
from src.transitions import Quadruple, Quintuple
from src.ReversibleTuringMachine import ReversibleTuringMachine

# Para rodar no windows:

# Comente as próximas duas linhas e
file = sys.stdin
content = file.readlines()

# descomente as próximas duas linhas.
#with open('entrada-quintupla.txt', 'r') as file:
#    content = file.readlines()
    
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
#print(' '.join(str_states))
for transition in transitions:
    print(transition)
    
reversibleTuringMachine = ReversibleTuringMachine(num_states, input_symbols, queue_symbols, transitions, entry)

reversibleTuringMachine.make_transitions()

print(reversibleTuringMachine)

reversibleTuringMachine.reverse_movement()

print(reversibleTuringMachine)
