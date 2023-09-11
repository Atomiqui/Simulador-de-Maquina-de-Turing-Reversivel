class Quadruple:
    def __init__(self, current_state, read_symbol, next_state, action):
        self.current_state = current_state
        self.read_symbol = read_symbol
        self.next_state = next_state
        self.action = action

    def __str__(self):
        return "({},{})=({},{})".format(self.current_state, self.read_symbol, self.next_state, self.action)