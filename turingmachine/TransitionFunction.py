DIRECTIONS = ['L', 'R', 'N']

class TransitionFunction:
    def __init__(self):
        # (состояние, символ) -> (новое состояние, символ для записи, направление)
        self.transitions = {}

    def add_transition(self, current_state, symbol, next_state, write_symbol, direction):
        if direction not in DIRECTIONS:
            raise ValueError(f"Invalid direction: {direction}. Must be 'L', 'R', or 'N'.")
        self.transitions[(current_state, symbol)] = (next_state, write_symbol, direction)

    def get_transition(self, current_state, symbol):
        if (current_state, symbol) not in self.transitions:
            raise KeyError(f"No transition defined for state '{current_state}' with symbol '{symbol}'")
        return self.transitions[(current_state, symbol)]
