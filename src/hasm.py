from hack_assembler import HackAssembler
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('asmfile', type=str, help='Input .asm file')
args = parser.parse_args()

assembler = HackAssembler(args.asmfile)
assembler.run()
for line in assembler.executable:
    print(line)

