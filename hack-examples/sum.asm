// TASK: 1 + 2 + 3 + ... + N  Iteratively
//
// iter = 1
// sum = 0
// (LOOP)
//      if (iter - N) > 0:
//          goto END_LOOP
//      sum += iter++;
// (END_LOOP)
//      R0 = sum
//      goto END

@iter
M = 0
@sum
M = 0
(LOOP)
    @iter
    D = M
    @R0
    D = D - M
    @END_LOOP
    D;JGT
    @iter
    D = M
    @sum
    M = M + D
    D = M
    @R1
    M = D
    @iter
    M = M + 1
    @LOOP
    0;JMP
(END_LOOP)
    @sum 
    D = M
    @R1
    M = D
    @END
    0;JMP
(END)
    @END
    0;JMP
