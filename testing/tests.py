import filecmp
import sys
sys.path.insert(0, '../src')
from hack_assembler import HackAssembler 

inputs = ["max.asm", "simple_add.asm", "mult.asm", 
          "pong.asm", "rect.asm", "fill.asm", "sum.asm"]

for program in inputs:
    assembler = HackAssembler(program)
    actual_file = assembler.get_actual_output() 
    expected_file = assembler.get_expected_output() 
    assembler.run()
   
    comp = filecmp.cmp(actual_file, expected_file, shallow = False)
    assert comp, "ASSERTION FAILED: " + program

print("TESTS PASSED")
