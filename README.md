# Assembler for the 16-bit Hack Assembly language
This project is part of the [nand2tetris](https://www.nand2tetris.org/) course.

# Quick Start
Pick a .asm file from ```hack-examples/``` dir
``` assembly
// Computes RAM[0] = 2 + 3
@2
D=A
@3
D=D+A
@0
M=D
```
Run the command:
```shell 
$ python3 run.py simple_add.asm 
``` 
The binary file is printed:
``` shell
0000000000000010
1110110000010000
0000000000000011
1110000010010000
0000000000000000
1110001100001000
```
You can also find the binary executable at ```testing/simple_add_actual.hack```. Now you can run it on hack hardware.
