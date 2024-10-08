from turingmachine import Alphabet, State, Tape, TransitionFunction, TuringMachine

if __name__ == '__main__':
    alphabet = Alphabet(symbols=['0', '1', '_'])

    state_q0 = State('q0')
    state_q1 = State('q1', is_final=True)
    inp = input("Введите последовательность нулей и единиц: ")
    if set(inp) != {'0', '1'}:
        print("Только нули и единицы!")
        exit(1)

    tape = Tape(inp)

    transition_function = TransitionFunction()
    transition_function.add_transition(state_q0, '0', state_q0, '1', 'R')
    transition_function.add_transition(state_q0, '1', state_q0, '1', 'R')
    transition_function.add_transition(state_q0, '_', state_q1, '_', 'N')

    machine = TuringMachine(tape, alphabet, state_q0, transition_function)

    machine.run()
    print(machine.tape)