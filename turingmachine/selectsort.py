from turingmachine import Tape, Alphabet, TransitionFunction, State, TuringMachine

# цифры и специальные символов
DIGITS = '0123456789'
START_SPECIAL_SYMBOL = 'S'
END_SPECIAL_SYMBOL = 'E'
REMOVED_SPECIAL_SYMBOL = 'X'
SPECIAL_SYMBOLS = {START_SPECIAL_SYMBOL, END_SPECIAL_SYMBOL, REMOVED_SPECIAL_SYMBOL}


def create_alphabet():
    return Alphabet(symbols=set(DIGITS).union(SPECIAL_SYMBOLS))


def create_tape(input_sequence):
    return Tape(input_string=START_SPECIAL_SYMBOL + input_sequence + END_SPECIAL_SYMBOL)


def create_states():
    state_start = State(name="start")
    state_halt = State(name="halt", is_final=True)
    state_comeback = State(name="comeback")
    return state_start, state_halt, state_comeback


def create_transition_function():
    return TransitionFunction()


def generate_comparing_and_printing_states():
    printing_states = []
    running_comparing_states = []
    removing_states = []
    comparing_states = {}

    for digit in DIGITS:
        printing_states.append(State(name=f"printing_{digit}"))
        running_comparing_states.append(State(name=f"comparing_{digit}"))
        comparing_states[int(digit)] = {}
        removing_states.append(State(name=f"removing_{digit}"))

        for another_digit in DIGITS + REMOVED_SPECIAL_SYMBOL:
            comparing_states[int(digit)][another_digit] = State(name=f"comparing_{digit}_to_{another_digit}")

    return printing_states, running_comparing_states, removing_states, comparing_states


def setup_transitions(transition_function, state_start, state_halt, printing_states, running_comparing_states,
                      removing_states, comparing_states, state_comeback):
    # начальное состояние: ищем первый символ после S
    transition_function.add_transition(state_start, START_SPECIAL_SYMBOL, state_start, START_SPECIAL_SYMBOL, 'R')  # пропускаем
    transition_function.add_transition(state_start, REMOVED_SPECIAL_SYMBOL, state_start, REMOVED_SPECIAL_SYMBOL, 'R')  # skip
    transition_function.add_transition(state_start, END_SPECIAL_SYMBOL, state_halt, END_SPECIAL_SYMBOL, 'R')  # halt
    transition_function.add_transition(state_start, '_', state_halt, '_', 'R')  # 404

    # running comp states from start
    for digit in DIGITS:
        transition_function.add_transition(state_start, digit, running_comparing_states[int(digit)], digit, 'R')

    # comp from running
    for digit in DIGITS:
        for another_digit in DIGITS + REMOVED_SPECIAL_SYMBOL:
            transition_function.add_transition(
                running_comparing_states[int(digit)],
                another_digit,
                comparing_states[int(digit)][another_digit],
                another_digit,
                'N'
            )

    # min running from comp
    for digit in DIGITS:
        transition_function.add_transition(
            comparing_states[int(digit)][REMOVED_SPECIAL_SYMBOL],
            REMOVED_SPECIAL_SYMBOL,
            running_comparing_states[int(digit)],
            REMOVED_SPECIAL_SYMBOL,
            'R'
        )

        for another_digit in DIGITS:
            if digit == another_digit:
                transition_function.add_transition(
                    comparing_states[int(digit)][another_digit],
                    another_digit,
                    running_comparing_states[int(digit)],
                    another_digit,
                    'R'
                )
            elif int(digit) < int(another_digit):
                transition_function.add_transition(
                    comparing_states[int(digit)][another_digit],
                    another_digit,
                    running_comparing_states[int(digit)],
                    another_digit,
                    'R'
                )
            else:
                transition_function.add_transition(
                    comparing_states[int(digit)][another_digit],
                    another_digit,
                    running_comparing_states[int(another_digit)],
                    another_digit,
                    'R'
                )

    # we are on the end
    for digit in DIGITS:
        transition_function.add_transition(
            running_comparing_states[int(digit)],
            END_SPECIAL_SYMBOL, removing_states[int(digit)], END_SPECIAL_SYMBOL, 'N'
        )

    # removing
    for digit in DIGITS:
        for another_digit in DIGITS + REMOVED_SPECIAL_SYMBOL + END_SPECIAL_SYMBOL:
            if digit != another_digit:
                transition_function.add_transition(
                    removing_states[int(digit)],
                    another_digit,
                    removing_states[int(digit)],
                    another_digit,
                    'L'
                )
            else:
                transition_function.add_transition(
                    removing_states[int(digit)],
                    another_digit,
                    printing_states[int(digit)],
                    REMOVED_SPECIAL_SYMBOL, 'R'
                )

    # printing
    for digit in DIGITS:
        for another_digit in DIGITS + START_SPECIAL_SYMBOL + END_SPECIAL_SYMBOL + REMOVED_SPECIAL_SYMBOL:
            transition_function.add_transition(
                printing_states[int(digit)],
                another_digit,
                printing_states[int(digit)],
                another_digit, 'R'
            )

        transition_function.add_transition(
            printing_states[int(digit)],
            '_',
            state_comeback,
            digit, 'L'
        )

    # comeback
    for digit in DIGITS + END_SPECIAL_SYMBOL + REMOVED_SPECIAL_SYMBOL:
        transition_function.add_transition(
            state_comeback,
            digit,
            state_comeback,
            digit,
            'L'
        )
    transition_function.add_transition(state_comeback, START_SPECIAL_SYMBOL, state_start, START_SPECIAL_SYMBOL, 'R')


def run_turing_machine(tape, alphabet, state_start, transition_function):
    turing_machine = TuringMachine(
        tape=tape,
        alphabet=alphabet,
        initial_state=state_start,
        transition_function=transition_function
    )

    # михалыч запускай дизель

    turing_machine.run()
    return turing_machine


def sort(inp):
    alphabet = create_alphabet()
    tape = create_tape(inp)
    state_start, state_halt, state_comeback = create_states()
    transition_function = create_transition_function()

    printing_states, running_comparing_states, removing_states, comparing_states = generate_comparing_and_printing_states()
    setup_transitions(transition_function, state_start, state_halt, printing_states, running_comparing_states,
                      removing_states, comparing_states, state_comeback)

    turing_machine = run_turing_machine(tape, alphabet, state_start, transition_function)
    return tape.slice_from_current_pos()

def main():
    input_sequence = '112331'

    alphabet = create_alphabet()
    tape = create_tape(input_sequence)
    state_start, state_halt, state_comeback = create_states()
    transition_function = create_transition_function()

    printing_states, running_comparing_states, removing_states, comparing_states = generate_comparing_and_printing_states()
    setup_transitions(transition_function, state_start, state_halt, printing_states, running_comparing_states,
                      removing_states, comparing_states, state_comeback)

    turing_machine = run_turing_machine(tape, alphabet, state_start, transition_function)

    print(f"Отсортированная лента: {tape}")
    print(f"Значимая часть ленты: {tape.slice_from_current_pos()}")
    print(f"Отсортированное питоном: {''.join(sorted(list(input_sequence)))}")
    print(f"NORMALNO OTSORTIROVAL?? {''.join(sorted(list(input_sequence))) == tape.slice_from_current_pos()}")


if __name__ == "__main__":
    main()
