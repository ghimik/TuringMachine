from turingmachine import Tape, Alphabet, TransitionFunction, State, TuringMachine
# создаем алфавит с дополнительным символом X
alphabet = Alphabet(symbols={'0', '1', 'X'})
input = '1101010100'
# создаем ленту с исходной последовательностью
tape = Tape(input_string=input)

state_start = State(name="start")
state_move_right = State(name="move_right")
state_find_zero = State(name="find_zero")
state_swap_to_zero = State(name="swap_to_zero")
state_return_to_x = State(name="return_to_x")
state_replace_x = State(name="replace_x")
state_halt = State(name="halt", is_final=True)


# создаем переходные функции
transition_function = TransitionFunction()

# переходы для состояния start: ищем первую 1 и помечаем ее как X
transition_function.add_transition(state_start, '0', state_start, '0', 'R')
transition_function.add_transition(state_start, '1', state_move_right, 'X', 'R')
transition_function.add_transition(state_start, '_', state_halt, '_', 'N')  # хальт, конец ленты

# состояние move_right: идем вправо, пока не найдем конец ленты
transition_function.add_transition(state_move_right, '0', state_move_right, '0', 'R')
transition_function.add_transition(state_move_right, '1', state_move_right, '1', 'R')
transition_function.add_transition(state_move_right, '_', state_find_zero, '_', 'L')  # мы в конце, ищем нуль

# состояние find_zero: ищем 0 слева, чтобы заменить его на 1
transition_function.add_transition(state_find_zero, '0', state_swap_to_zero, '1', 'N')
transition_function.add_transition(state_find_zero, '1', state_find_zero, '1', 'L')
transition_function.add_transition(state_find_zero, 'X', state_return_to_x, 'X', 'L')  # нашли X, возвращаемся к нему

# состояние swap_to_zero: меняем найденный 0 на 1 и возвращаемся к X
transition_function.add_transition(state_swap_to_zero, '_', state_return_to_x, '_', 'L')
transition_function.add_transition(state_swap_to_zero, '0', state_swap_to_zero, '0', 'L')
transition_function.add_transition(state_swap_to_zero, '1', state_return_to_x, '1', 'L')

# состояние return_to_x: возвращаемся к X
transition_function.add_transition(state_return_to_x, '0', state_return_to_x, '0', 'L')
transition_function.add_transition(state_return_to_x, '1', state_return_to_x, '1', 'L')
transition_function.add_transition(state_return_to_x, 'X', state_start, '0', 'R')  # по новой
transition_function.add_transition(state_return_to_x, '_', state_replace_x, '_', 'R')  # если достигли конца, останавливаемся

transition_function.add_transition(state_replace_x, '0', state_replace_x, '0', 'R')
transition_function.add_transition(state_replace_x, '1', state_replace_x, '1', 'R')
transition_function.add_transition(state_replace_x, 'X', state_replace_x, '1', 'R')
transition_function.add_transition(state_replace_x, '_', state_halt, '_', 'N')


turing_machine = TuringMachine(
    tape=tape,
    alphabet=alphabet,
    initial_state=state_start,
    transition_function=transition_function
)

turing_machine.run()

print(f"Отсортированная лента: {tape}")
print(f"Отсортированная питоном лента: {''.join(sorted(list(input)))}")


