# Grupo: Alisson Costa Schmidt, Gabriel e Leonardo.

import sys
from copy import copy

def parse_quintuple(transition):
    current_state, read_symbol = transition[transition.index("(") + 1:transition.index(")")].split(",")
    transition = transition[transition.index("=") + 1:]
    next_state, write_symbol, head_movement = transition[transition.index("(") + 1:transition.index(")")].split(",")

    return current_state, read_symbol, next_state, write_symbol, head_movement

def create_quadruples(transitions):
    quadruples = []
    for transition in transitions:
        current_state, read_symbol, next_state, write_symbol, head_movement = parse_quintuple(transition)
        q1 = (current_state, read_symbol, next_state + "*", write_symbol)
        q2 = (next_state + "*", write_symbol, next_state, head_movement)
        quadruples.extend([q1, q2])
    return quadruples

def make_transitions(quadruples, entry):
    state_marker = quadruples[0][0]
    head_marker = 0

    input_tape = list(entry + "B")
    history_tape = []
    output_tape = []
    final_state = quadruples[-1][2]

    step = 0

    while state_marker != final_state:
        nt = 0
        for quadruple in quadruples:
            if state_marker == quadruple[0]:
                if input_tape[head_marker] == quadruple[1]:
                    state_marker = quadruple[2]
                    if quadruple[3] == "L":
                        head_marker -= 1
                    elif quadruple[3] == "R":
                        head_marker += 1
                    else:
                        input_tape[head_marker] = quadruple[3]
                    history_tape.append(nt)
                    step += 1

                    # Print das transições
                    print(f"Passo {step}:")
                    print("Histórico:", history_tape)
                    print("Output:", output_tape)
                    print("---")

            nt += 1

    output_tape = copy(input_tape)
    accepted = state_marker == final_state  # Check if in final state
    return input_tape, history_tape, output_tape, accepted

def reverse_movement(history_tape, quadruples, input_tape, head_marker):
    i = len(history_tape) - 1
    step = 0

    while i >= 0:
        q = history_tape[i]
        if quadruples[q][3] == "R":
            head_marker -= 1
        elif quadruples[q][3] == "L":
            head_marker += 1
        else:
            input_tape[head_marker] = quadruples[q][1]
        i -= 1
        history_tape.pop()
        step += 1

        # Print da reversão
        print(f"Passo {step} da reversão:")
        print("Histórico:", history_tape)
        print("Output:", output_tape)
        print("---")

# Printa a MT lida para confirmar que está lendo corretamente.
def print_mt_info(num_states, num_input_symbols, num_queue_symbols, num_transitions, str_states, input_symbols, queue_symbols, transitions):
    print("MT Lida:\n")
    print(f"{num_states} {num_input_symbols} {num_queue_symbols} {num_transitions}")
    print(' '.join(str_states))
    print(' '.join(input_symbols))
    print(' '.join(queue_symbols))
    for transition in transitions:
        print(transition)

## Para rodar no Windows:
## Comente as próximas duas linhas e
file = sys.stdin
content = file.readlines()

## descomente as próximas duas linhas.
# with open('entrada-quintupla.txt', 'r') as file:
#     content = file.readlines()

num_states, num_input_symbols, num_queue_symbols, num_transitions = content[0].split()
str_states = content[1].split()
input_symbols = content[2].split()
queue_symbols = content[3].split()
transitions = []

for i in range(4, 4 + int(num_transitions)):
    transitions.append(content[i])

entry = content[-1]

# print_mt_info(num_states, num_input_symbols, num_queue_symbols, num_transitions, str_states, input_symbols, queue_symbols, transitions)

quadruples = create_quadruples(transitions)

input_tape, history_tape, output_tape, accepted = make_transitions(quadruples, entry)

if accepted:
    print("\nAceitou!")
else:
    print("\nRejeitou!")

print("\nApós as transições:\n")
print("Entrada:", input_tape)
print("Histórico:", history_tape)
print("Output:", output_tape)
print("\n")

reverse_movement(history_tape, quadruples, input_tape, 0)

print("\nApós reversão do movimento:\n")
print("Entrada:", input_tape)
print("Histórico:", history_tape)
print("Output:", output_tape)