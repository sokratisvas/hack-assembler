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

(LOOP)
    @KBD
    D = M
    @WHITE
    D;JEQ
    @SCREEN
    D = A
    @row_idx
    M = D
    (BLACK_LOOP)
        @row_idx
        D = M
        @24575
        D = D - A
        @BLACK_LOOP_END
        D;JGT
        @row_idx
        A = M
        M = -1
        @row_idx
        M = M + 1
        @BLACK_LOOP
        0;JMP
    (BLACK_LOOP_END)
        @LOOP
        0;JMP
    (WHITE)
        @SCREEN
        D = A
        @row_idx
        M = D
        (WHITE_LOOP)
            @row_idx
            D = M
            @24575
            D = D - A
            @WHITE_LOOP_END
            D;JGT
            @row_idx
            A = M 
            M = 0
            @row_idx
            M = M + 1
            @WHITE_LOOP
            0;JMP
        (WHITE_LOOP_END)
            @LOOP
            0;JMP


