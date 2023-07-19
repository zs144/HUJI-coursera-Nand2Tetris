import os
import SymbolTable
import Code

def get_comment_location(instruction : str) -> int:
    loc = -1
    for i in range(len(instruction) - 1):
        if ((instruction[i] == '/') & (instruction[i+1] == '/')):
            loc = i
            break
    return loc


def get_pure_assembly(f_in) -> list:
    assembly = []
    for line in f_in.readlines():
        line = line.strip()
        if len(line) != 0:
            comment_location = get_comment_location(line)
            if comment_location == -1:
                assembly.append(line)
            elif comment_location == 0:
                pass
            else:
                assembly.append(line[:comment_location].strip())
    return assembly


def instructionType(s : str) -> str:
    if (s[0] == '@'):
        return "A"
    else:
        return "C"


class HackAssember:
    # Initialize
    def __init__(self, src_filename) -> None:
        path = os.path.dirname(__file__)
        src_filename = os.path.join(path, src_filename)
        f_in = open(src_filename, 'r')
        self.filename_nosuffix = src_filename.split('.')[0]
        self.symbol_table = SymbolTable.SymbolTable("symbols.txt")
        self.assembly = get_pure_assembly(f_in)
        self.binary_code = []
        self.closest_available_reg = 16
        f_in.close()

    def parse_A_instruction(self, instruction : str) -> str:
        field = instruction[1:]
        mem_location = 0
        if (self.symbol_table.contains(field)):
            mem_location = self.symbol_table.get_address(field)
        else:
            if (field.isdigit()):
                mem_location = int(field)
            else:
                mem_location = self.closest_available_reg
                self.symbol_table.add_entry(symbol=field, address=mem_location)
                self.closest_available_reg += 1
        return f"{mem_location:b}".rjust(16, '0')


    def parse_C_instruction(self, instruction : str) -> str:
        dest_field, comp_field, jump_field = None, None, None
        if '=' in instruction:
            dest_field = instruction.split('=')[0]
            comp_field = instruction.split('=')[1]
            jump_field = None
        else:
            comp_field = instruction.split(';')[0]
            jump_field = instruction.split(';')[1]
            dest_field = None
        dest_code = Code.dest(dest_field)
        comp_code = Code.comp(comp_field)
        jump_code = Code.jump(jump_field)
        return "111" + comp_code + dest_code + jump_code


    def parse(self):
        # First pass
        num_label = 0
        for i in range(len(self.assembly)):
            instruction = self.assembly[i]
            if instruction[0] == '(':
                label = instruction[1:-1]
                self.symbol_table.add_entry(symbol=label, address=i-num_label)
                num_label += 1
        self.assembly[:] = [s for s in self.assembly if s[0] != '(']

        # Second pass
        for instruction in self.assembly:
            if (instructionType(instruction) == 'A'):
                self.binary_code.append(self.parse_A_instruction(instruction))
            else:
                self.binary_code.append(self.parse_C_instruction(instruction))

    # Export the output to a .hack file
    def export_binary_code(self):
        path = os.path.dirname(__file__)
        out_filename = self.filename_nosuffix + ".hack"
        out_filename = os.path.join(path, out_filename)
        f_out = open(out_filename, 'w')
        for s in self.binary_code:
            f_out.write(s+"\n")
        f_out.close()


def main():
    assembler = HackAssember(src_filename=input("Enter the src code filename: "))
    assembler.parse()
    assembler.export_binary_code()


if __name__ == "__main__":
    main()
