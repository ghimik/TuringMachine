from turingmachine import Tape, Alphabet, TransitionFunction


class TuringMachine:
    def __init__(self, tape: Tape, alphabet: Alphabet, states, initial_state,
                 transition_function: TransitionFunction):
        self.tape = tape
        self.alphabet = alphabet
        self.states = states
        self.current_state = initial_state
        self.transition_function = transition_function

    def step(self):
        current_symbol = self.tape.read()
        if not self.alphabet.is_valid_symbol(current_symbol):
            raise ValueError(f"Invalid symbol on tape: {current_symbol}")

        next_state, write_symbol, direction = self.transition_function.get_transition(self.current_state, current_symbol)
        self.tape.write(write_symbol)

        if direction == 'L':
            self.tape.move_left()
        elif direction == 'R':
            self.tape.move_right()

        self.current_state = next_state

    def run(self):
        while not self.current_state.is_final:
            self.step()
        print(f"Machine halted in state: {self.current_state}")
        print("Final tape content:", self.tape)
