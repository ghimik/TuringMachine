from turingmachine import Tape


class TuringMachine:
    def __init__(self, tape: Tape, states, initial_state, final_states, transition_function):
        self.tape = tape
        self.states = states
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function  # Функция переходов в виде словаря

    def step(self):
        current_symbol = self.tape.read()
        if (self.current_state, current_symbol) not in self.transition_function:
            raise Exception(f"No rule for state '{self.current_state}' with symbol '{current_symbol}'")

        next_state, write_symbol, direction = self.transition_function[(self.current_state, current_symbol)]
        self.tape.write(write_symbol)

        if direction == 'L':
            self.tape.move_left()
        elif direction == 'R':
            self.tape.move_right()

        self.current_state = next_state

    def run(self):
        while self.current_state not in self.final_states:
            self.step()
        print("Machine halted in state:", self.current_state)
        print("Final tape content:", self.tape)

