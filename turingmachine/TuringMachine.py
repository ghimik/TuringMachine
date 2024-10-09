from turingmachine import Tape, Alphabet, TransitionFunction
from turingmachine.configs import DEBUG

class TuringMachine:
    def __init__(self, tape: Tape, alphabet: Alphabet, initial_state,
                 transition_function: TransitionFunction):
        self.tape = tape
        self.alphabet = alphabet
        self.current_state = initial_state
        self.transition_function = transition_function

    def step(self):
        current_symbol = self.tape.read()
        if not self.alphabet.is_valid_symbol(current_symbol):
            raise ValueError(f"Invalid symbol on tape: {current_symbol}")

        next_state, write_symbol, direction = self.transition_function.get_transition(self.current_state, current_symbol)
        if DEBUG:
            print('STEP START')
            print(f'Tape: {self.tape}')
            print(f'State: {self.current_state}')
        self.tape.write(write_symbol)

        if direction == 'L':
            self.tape.move_left()
        elif direction == 'R':
            self.tape.move_right()

        self.current_state = next_state
        if DEBUG:
            print('TO')
            print(f'Tape: {self.tape}')
            print(f'State: {self.current_state}')
            print('STEP END')

    def run(self):
        while not self.current_state.is_final:
            self.step()
        print(f"Machine halted in state: {self.current_state}")
        print("Final tape content:", self.tape)
