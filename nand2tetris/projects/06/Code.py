DEST_SPEC = {}
DEST_SPEC[None]   = "000"
DEST_SPEC["M"]    = "001"
DEST_SPEC["D"]    = "010"
DEST_SPEC["DM"]   = "011"
DEST_SPEC["A"]    = "100"
DEST_SPEC["AM"]   = "101"
DEST_SPEC["AD"]   = "110"
DEST_SPEC["ADM"]  = "111"


JUMP_SPEC = {}
JUMP_SPEC[None]  = "000"
JUMP_SPEC["JGT"] = "001"
JUMP_SPEC["JEQ"] = "010"
JUMP_SPEC["JGE"] = "011"
JUMP_SPEC["JLT"] = "100"
JUMP_SPEC["JNE"] = "101"
JUMP_SPEC["JLE"] = "110"
JUMP_SPEC["JMP"] = "111"

COMP_SPEC = {}
COMP_SPEC["0"]   = "0101010"
COMP_SPEC["1"]   = "0111111"
COMP_SPEC["-1"]  = "0111010"
COMP_SPEC["D"]   = "0001100"
COMP_SPEC["A"]   = "0110000"
COMP_SPEC["!D"]  = "0001101"
COMP_SPEC["!A"]  = "0110001"
COMP_SPEC["-D"]  = "0001111"
COMP_SPEC["-A"]  = "0110011"
COMP_SPEC["D+1"] = "0011111"
COMP_SPEC["A+1"] = "0110111"
COMP_SPEC["D-1"] = "0001110"
COMP_SPEC["A-1"] = "0110010"
COMP_SPEC["D+A"] = "0000010"
COMP_SPEC["D-A"] = "0010011"
COMP_SPEC["A-D"] = "0000111"
COMP_SPEC["D&A"] = "0000000"
COMP_SPEC["D|A"] = "0010101"
COMP_SPEC["M"]   = "1110000"
COMP_SPEC["!M"]  = "1110001"
COMP_SPEC["-M"]  = "1110011"
COMP_SPEC["M+1"] = "1110111"
COMP_SPEC["M-1"] = "1110010"
COMP_SPEC["D+M"] = "1000010"
COMP_SPEC["D-M"] = "1010011"
COMP_SPEC["M-D"] = "1000111"
COMP_SPEC["D&M"] = "1000000"
COMP_SPEC["D|M"] = "1010101"

def dest(field) -> str:
    return DEST_SPEC[field]

def comp(field) -> str:
    return COMP_SPEC[field]

def jump(field) -> str:
    return JUMP_SPEC[field]

def main():
    # Testing:
    print(dest("DM"))
    print(comp("D&M"))
    print(jump("JNE"))
    print(dest(None))
    print(jump(None))

if __name__ == "__main__":
    main()