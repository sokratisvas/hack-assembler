from binary_syntax import *

def instruction_type(instruction):            
    return 'A' if instruction.startswith('@') else 'C'

def get_components(C_instruction):
    assert instruction_type(C_instruction) == 'C'
    if '=' in C_instruction:
        dest, comp = C_instruction.split('=', 1)
        jump = 'null'
    else:
        comp, jump = C_instruction.split(';', 1)
        dest = 'null'
    return dest, comp, jump

class HackAssembler:
    def __init__(self, filename):
        self.filename = filename
        self.symbols = {                                 
            "SCREEN": 16384, "KBD": 24576, "SP": 0,  
            "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4 
        }
                   
        for i in range(16): 
            self.symbols['R' + str(i)] = i

        self.executable = []
        self.tokens = []
        self.labels = []

    def get_actual_output(self):
        return "../testing/" + self.filename[:-4] + "_actual" + ".hack"

    def get_expected_output(self):
        return "../testing/" + self.filename[:-4] + "_expected" + ".hack"

    def tokenize(self):
        filepath = "../hack-examples/" + self.filename
        with open(filepath, mode = 'r', encoding = "utf-8") as f:
            self.tokens = [line.strip().replace(' ', '') for line in f if line.strip()[:2] != "//" and line.strip()]
            for i in range(len(self.tokens)):
                self.tokens[i] = self.tokens[i].split('//', 1)[0]
            self.labels = [token for token in self.tokens if token.startswith('(') and token.endswith(')')]
        for label in self.labels:
            self.symbols[label[1:-1]] = self.tokens.index(label) - self.labels.index(label) 
        for label in self.labels:
            self.tokens.remove(label)
    
    def update_variables(self):
        mem_address = 16
        for token in self.tokens:
            if token.startswith('@') and not token[1:].isdigit():
                if token[1:] not in self.symbols:
                    self.symbols[token[1:]] = mem_address
                    mem_address += 1
    
    def generate_code(self):
        for token in self.tokens:  
            if instruction_type(token) == 'A':
                if token[1:].isdigit():
                    self.executable.append("{0:016b}".format(int(token[1:]))) 
                else: 
                    self.executable.append("{0:016b}".format(self.symbols[token[1:]]))
            else:
                dest, cost, jump = get_components(token)
                self.executable.append('111' + a_syntax[cost] + comp_syntax[cost] 
                                    + dest_syntax[dest] + jump_syntax[jump])
    
    def write_output(self):
        filepath = self.get_actual_output()
        with open(filepath, mode = 'w', encoding = "utf-8") as f:
            for line in self.executable:
                f.write(line + '\n')

    def run(self):
        self.tokenize()
        self.update_variables()
        self.generate_code()
        self.write_output()

