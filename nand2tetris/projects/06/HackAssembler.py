import os
import SymbolTable

def HackAssembler(src_filename : str):
    # Initialize
    path = os.path.dirname(__file__)
    src_filename = os.path.join(path, src_filename)
    f = open(src_filename, 'r')
    symbol_table = SymbolTable.SymbolTable("symbols.txt")

    # First pass
    
    # Second pass