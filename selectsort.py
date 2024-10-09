from turingmachine import Tape, Alphabet, TransitionFunction, State, TuringMachine


# создаем алфавит
alphabet = Alphabet(symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'E', 'X'})
input_sequence = '537831913434322'
tape = Tape(input_string='S'+input_sequence+'E')

# создаем начальные состояния
state_start = State(name="start")
state_halt = State(name="halt", is_final=True)

state_comeback = State(name="comeback")

# массивы для состояний
printing_states = []
running_comparing_states = []
removing_states = []
comparing_states = {}


# создаем переходные функции
transition_function = TransitionFunction()

# генерируем состояния для сравнения и печати
for digit in '0123456789':
    # состояния для печати минимальной цифры
    printing_states.append(State(name=f"printing_{digit}"))

    # состояния для сравнения цифр
    running_comparing_states.append(State(name=f"comparing_{digit}"))
    comparing_states[int(digit)] = {}


    removing_states.append(State(name=f"removing_{digit}"))

    for another_digit in '0123456789X':
        # состояния для сравнения между двумя цифрами
        comparing_states[int(digit)][another_digit] =\
            State(name=f"comparing_{digit}_to_{another_digit}")



# начальное состояние: ищем первый символ после S
transition_function.add_transition(state_start, 'S', state_start, 'S', 'R')  # пропускаем
transition_function.add_transition(state_start, 'X', state_start, 'X', 'R') # skip
transition_function.add_transition(state_start, 'E', state_halt, 'E', 'R')  # halt
transition_function.add_transition(state_start, '_', state_halt, '_', 'R') # 404
# running comp states from start
for digit in '0123456789':
    transition_function.add_transition(state_start, digit, running_comparing_states[int(digit)], digit, 'R')

# comp from running
for digit in '0123456789':
    for another_digit in '0123456789X':
        transition_function.add_transition(running_comparing_states[int(digit)], another_digit,
                                           comparing_states[int(digit)][another_digit], another_digit, 'N')

#min running from comp
for digit in '0123456789':
    transition_function.add_transition(
        comparing_states[int(digit)]['X'],
        'X',
        running_comparing_states[int(digit)],
        'X',
        'R'
    )

    for another_digit in '0123456789':
        # Переход для равных цифр
        if digit == another_digit:
            transition_function.add_transition(
                comparing_states[int(digit)][another_digit],
                another_digit,
                running_comparing_states[int(digit)],
                another_digit,
                'R'
            )
        # Переход для меньше/больше
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
for digit in '0123456789':
    transition_function.add_transition(running_comparing_states[int(digit)],
                                       'E', removing_states[int(digit)],'E' ,'N')

#removing
for digit in '0123456789':
    for another_digit in '0123456789EX':
        if digit != another_digit:
            transition_function.add_transition(removing_states[int(digit)], another_digit,
                                               removing_states[int(digit)], another_digit, 'L')
        else:
            transition_function.add_transition(removing_states[int(digit)], another_digit,
                                               printing_states[int(digit)], 'X', 'R')

#printing
for digit in '0123456789':
    for another_digit in '0123456789ESX':
        transition_function.add_transition(printing_states[int(digit)], another_digit,
                                           printing_states[int(digit)], another_digit,'R')

    transition_function.add_transition(printing_states[int(digit)], '_',
                                       state_comeback, digit, 'L')

#comeback
for digit in '0123456789EX':
    transition_function.add_transition(state_comeback, digit, state_comeback, digit, 'L')
transition_function.add_transition(state_comeback, 'S', state_start, 'S', 'R')


turing_machine = TuringMachine(
    tape=tape,
    alphabet=alphabet,
    initial_state=state_start,
    transition_function=transition_function
)

# михалыч запускай дизель
turing_machine.run()

print(f"Отсортированная лента: {tape}")
print(f"Значимая часть ленты: {tape.slice_from_current_pos()}")
print(f"Отсортированное питоном: {''.join(sorted(list(input_sequence)))}")
print(f"NORMALNO OTSORTIROVAL?? {''.join(sorted(list(input_sequence))) == tape.slice_from_current_pos()}")