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

    def __str__(self):
        return ''.join(self.tape).strip(self.blank_symbol)
