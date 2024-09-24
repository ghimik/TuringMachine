from turingmachine import Alphabet, State, Tape, TransitionFunction, TuringMachine

if __name__ == '__main__':
    alphabet = Alphabet(symbols=['0', '1', '_'])

    state_q0 = State('q0')
    state_q1 = State('q1', is_final=True)
    states = {state_q0, state_q1}

    tape = Tape("11111")

    transition_function = TransitionFunction()
    transition_function.add_transition(state_q0, '1', state_q0, '0', 'R')
    transition_function.add_transition(state_q0, '_', state_q1, '_', 'N')

    machine = TuringMachine(tape, alphabet, states, state_q0, transition_function)

    machine.run()
