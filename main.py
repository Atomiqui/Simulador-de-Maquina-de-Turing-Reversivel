#Grupo:
#Alisson, Ana, Francisco e Enzo.

import sys
from Quintuple import Quintuple
from ReversibleTuringMachine import ReversibleTuringMachine

file = sys.stdin
content = file.readlines()

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
    
reversibleTuringMachine = ReversibleTuringMachine(num_states, input_symbols, queue_symbols, transitions, entry)

reversibleTuringMachine.make_transitions()

print(reversibleTuringMachine)

reversibleTuringMachine.reverse_movement()

print(reversibleTuringMachine)