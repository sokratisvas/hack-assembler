from hack_assembler import HackAssembler

import sys

assembler = HackAssembler(sys.argv[1])
assembler.run()
for line in assembler.executable:
    print(line)

