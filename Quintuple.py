from Quadruple import Quadruple

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