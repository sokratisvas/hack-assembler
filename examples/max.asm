// TASK: R0 = max(R1, R2)
// if (R1 > R2) then R0 = R1
// else R0 = R2

// if (R1 - R2 >= 0) goto POS1
@R1
D = M
@R2
D = D - M 
@POS
D;JGE
// R1 - R2 < 0
@R2
D = M
@R0
M = D
//goto END
@END
0;JMP
(POS)
    //R1 - R2 >= 0
    @R1
    D = M 
    @R0
    M = D
(END)
    @END
    0;JMP

