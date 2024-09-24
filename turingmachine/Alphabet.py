class Alphabet:
    def __init__(self, symbols, blank_symbol='_'):
        self.symbols = set(symbols)
        self.blank_symbol = blank_symbol

        if blank_symbol not in self.symbols:
            self.symbols.add(blank_symbol)

    def is_valid_symbol(self, symbol):
        return symbol in self.symbols
