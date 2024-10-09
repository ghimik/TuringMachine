from turingmachine.configs import DEBUG

class Tape:
    def __init__(self, input_string='', blank_symbol='_'):
        self.blank_symbol = blank_symbol
        self.tape = list(input_string) if input_string else [blank_symbol]
        self.head_position = 0

    def read(self):
        if self.head_position < 0 or self.head_position >= len(self.tape):
            return self.blank_symbol
        return self.tape[self.head_position]

    def write(self, symbol):
        if self.head_position < 0:
            self.tape = [self.blank_symbol] * (-self.head_position) + self.tape
            self.head_position = 0
        elif self.head_position >= len(self.tape):
            self.tape.extend([self.blank_symbol] * (self.head_position - len(self.tape) + 1))
        self.tape[self.head_position] = symbol

    def move_left(self):
        self.head_position -= 1

    def move_right(self):
        self.head_position += 1

    def slice_from_current_pos(self):
        return ''.join(self.tape[self.head_position::])

    def __str__(self):
        if DEBUG:
            # Создаем новый список для отображения ленты с выделенным текущим символом
            display_tape = []
            for i in range(len(self.tape)):
                if i == self.head_position:
                    # Выделяем текущий символ
                    display_tape.append(f'[{self.tape[i]}]')
                else:
                    display_tape.append(self.tape[i])
            return ''.join(display_tape).strip(self.blank_symbol)
        else:
            return ''.join(self.tape).strip(self.blank_symbol)
