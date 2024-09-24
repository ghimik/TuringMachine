from turingmachine import Tape, TuringMachine

if __name__ == '__main__':
    tape = Tape("11111", blank_symbol='_')

    states = {'q0', 'q1', 'halt'}
    initial_state = 'q0'
    final_states = {'halt'}

    transition_function = {
        ('q0', '1'): ('q0', '0', 'R'),
        ('q0', '_'): ('halt', '_', 'N'),
    }

    machine = TuringMachine(tape, states, initial_state, final_states, transition_function)

    machine.run()
