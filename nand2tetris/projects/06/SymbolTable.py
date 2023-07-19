import os

class SymbolTable:
    def __init__(self, filename : str) -> None:
        path = os.path.dirname(__file__)
        filename = os.path.join(path, filename)
        self.symbols = {}
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            pair = line.strip().split(",")
            self.symbols[pair[0]] = int(pair[1])

    def contains(self, symbol : str) -> bool:
        return symbol in self.symbols.keys()

    def add_entry(self, symbol : str, address : int):
        if ~ self.contains(symbol):
            self.symbols[symbol] = address

    def get_address(self, symbol : str) -> int:
        if self.contains(symbol):
            return self.symbols[symbol]
        else:
            raise KeyError("The symbol is not recorded in the symbol table.")


def main():
    # Testing:
    symbol_table = SymbolTable("symbols.txt")
    symbol_table.add_entry("R30", 30)
    print(symbol_table.symbols)

if __name__ == "__main__":
    main()