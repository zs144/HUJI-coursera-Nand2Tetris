// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// Pseudo-code:
// while True {
//     color = -1;
//     if (RAM[KYB] == 0) {
//         color = 0;
//     }
//     i = 0;
//     screen_pixels = 8192;
//     ptr = SCREEN;
//     while (i < screen_pixels) {
//         RAM[ptr] = color;
//         ptr += 1;
//         i++;
//     }
// }

// while True
(OUTER_LOOP)
    // color = -1;
    @color
    M=-1 // black color

    // if (RAM[KYB] == 0)
    @KBD
    D=M
    @ELSE
    D;JEQ
    (END_IF)

    // i = 0;
    @i
    M=0

    // screen_pixels = 8192;
    @8192
    D=A
    @screen_pixels
    M=D

    // ptr = SCREEN;
    @SCREEN
    D=A
    @ptr
    M=D

    // while (i < screen_pixels)
    (INNER_LOOP)
        @i
        D=M
        @screen_pixels
        D=D-M
        @INNER_END
        D;JGE
        // RAM[ptr] = color;
        @color
        D=M
        @ptr
        A=M
        M=D
        // ptr += 1;
        @ptr
        M=M+1
        // i++;
        @i
        M=M+1
        @INNER_LOOP
        0;JMP

    (INNER_END)
        @OUTER_END

    (OUTER_END)
        @OUTER_LOOP
        0;JMP

    // else
    (ELSE)
        // color = 0;
        @color
        M=0 // white color
        @END_IF
        0;JMP