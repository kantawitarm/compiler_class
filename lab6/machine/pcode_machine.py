"""The P-code machine module."""


# -----------------------------------------------------------------------------
DEFAULT_INSTRUCTION = (0,0,0) #! EDIT FROM 0 => (0,0,0)
DEFAULT_INSTRUCTION_MEMORY_SIZE = 200

DEFAULT_DATA = hex(0x0) #! 0 -> hex(00)
DEFAULT_DATA_MEMORY_SIZE = 500

DEFAULT_REGISTER = 0


# -----------------------------------------------------------------------------
class PCodeMachineEmulator:
    """The P-code machine emulator."""

    def __init__(self):
        """Construct a P-code machine emulator."""
        # Memory
        self.instruction_memory = \
            [DEFAULT_INSTRUCTION] * DEFAULT_INSTRUCTION_MEMORY_SIZE
        self.data_memory = [DEFAULT_DATA]*DEFAULT_DATA_MEMORY_SIZE

        # Registers
        self.program_counter = DEFAULT_REGISTER
        self.base_pointer = DEFAULT_REGISTER
        self.top_of_stack = DEFAULT_REGISTER

    def dump(self):
        """Dump the machine contents."""

        # print(self.data_memory)


        dump_data = \
        "P-Code Machine\n"          \
        "Registers\n"               \
        f"Program counter:   {self.program_counter}\n"    \
        f"Base pointer:      {self.base_pointer}\n"    \
        f"Top of stack:      {self.top_of_stack}\n"    \
        "\n"                        \
        "Instruction memory\n"

        # NOTE: INSTRUCTION_MEMORY
        # print(self.instruction_memory)
        data_instruction_memory = ""
        # count = 0
        for i in range(len(self.instruction_memory)):
            data_instruction_memory += str(self.instruction_memory[i])
            #NOTE: make 00
            # if( (i + 1) % 3 == 0):
            #     count +=1
            if( (i + 1) % 10 == 0):
                data_instruction_memory += "\n"
            elif( (i + 1) % 1 == 0):
                data_instruction_memory += " "
        
        # print(data_instruction_memory)
        data_instruction_memory += "\n"
        dump_data += data_instruction_memory

        # NOTE: data_memory
        data_memory = "Data memory\n"

        for i in range(len(self.data_memory)):
            data_memory += str(self.data_memory[i])
            #NOTE: make 00
            if( (i + 1) % 10 == 0):
                data_memory += "\n"
            elif( (i + 1) % 1 == 0):
                data_memory += " "

        print(data_memory)
        # dump_data += data_memory

        # print(dump_data)

        return dump_data

    # TODO: ------------------------
    #   function base(l: integer): integer;
    #     var b1: integer;
    #   begin
    #     b1 := b; {find base l levels down}
    #     while l > 0 do begin
    #       b1 := s[b1];
    #       l := l - 1
    #     end;
    #     base := b1
    #   end {base};

    def base(self, l:int) -> int:
        b1 = self.base_pointer
        while l > 0:
            b1 = self.data_memory[b1]
            l = l-1
        
        return b1


    # TODO: ------------------------

    def load_program(self, list_of_pcode: list):
        """Load program into instruction memory."""
        if len(list_of_pcode) > len(self.instruction_memory):
            raise ValueError("Too many instructions to be held in the memory.")

        for index, value in enumerate(list_of_pcode):
            self.instruction_memory[index] = value

    def step(self, function, level, constant):
        """Execute one instruction."""
        if(function == "lit"):
            self.top_of_stack +=1
            self.data_memory[self.top_of_stack] = constant
            pass

        elif(function == "opr"):
            # case a of {operator}
            # opr 0, a  : execute operation a (13 operations: RETURN, 5 math functions, and 7 comparison functions)
            operator = constant
            if(operator == 0):
                # t := b - 1; p := s[t + 3]; b := s[t + 2];
                self.top_of_stack = self.base_pointer -1
                self.program_counter = self.data_memory[self.top_of_stack +3]
                self.base_pointer = self.data_memory[self.top_of_stack +2]
                pass
            elif (operator == 1): #TODO: flip + -> - , - -> +
                # 1: s[t] := -s[t];
                self.data_memory[self.top_of_stack] = -self.data_memory[self.top_of_stack]
                pass
            elif (operator == 2): #TODO: ADD
                # 2: begin t := t - 1; s[t] := s[t] + s[t + 1] end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = self.data_memory[self.top_of_stack] + self.data_memory[self.top_of_stack + 1]
                pass
            elif (operator == 3): #TODO: SUB
                # 3: begin t := t - 1; s[t] := s[t] - s[t + 1] end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = self.data_memory[self.top_of_stack] - self.data_memory[self.top_of_stack + 1]
                pass
            elif (operator == 4): #TODO: MUL
                # 4: begin t := t - 1; s[t] := s[t] * s[t + 1] end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = self.data_memory[self.top_of_stack]  * self.data_memory[self.top_of_stack + 1] 
                pass
            elif (operator == 5): #TODO: DIV
                # 5: begin t := t - 1; s[t] := s[t] div s[t + 1] end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = self.data_memory[self.top_of_stack] / self.data_memory[self.top_of_stack+1]
                pass
            elif (operator == 6): #TODO: flip + -> - , - -> +
                # 6: s[t] := ord(odd(s[t]));
                # TODO: CHECK IS ODD NUMBER
                self.data_memory = bool((self.data_memory[self.top_of_stack]) %2 == 0)
                pass
            elif (operator == 8): #TODO: EQU
                # 8: begin t := t - 1; s[t] := ord(s[t] = s[t + 1]) end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = bool(self.data_memory[self.top_of_stack] == self.data_memory[self.top_of_stack+1])
                pass
            elif (operator == 9): #TODO: NEQ
                # 9: begin t := t - 1; s[t] := ord(s[t] <> s[t + 1]) end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = bool(self.data_memory[self.top_of_stack] != self.data_memory[self.top_of_stack+1])
                pass
            elif (operator == 10): #TODO: LSS
                # 10: begin t := t - 1; s[t] := ord(s[t] < s[t + 1]) end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = bool(self.data_memory[self.top_of_stack] < self.data_memory[self.top_of_stack+1])
                pass
            elif (operator == 11): #TODO: GEQ
                # 11: begin t := t - 1; s[t] := ord(s[t] >= s[t + 1]) end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = bool(self.data_memory[self.top_of_stack] >= self.data_memory[self.top_of_stack+1])
                pass
            elif (operator == 12): #TODO: GTR
                # 12: begin t := t - 1; s[t] := ord(s[t] > s[t + 1]) end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = bool(self.data_memory[self.top_of_stack] > self.data_memory[self.top_of_stack+1])
                pass
            elif (operator == 13): #TODO: LEQ
                # 13: begin t := t - 1; s[t] := ord(s[t] <= s[t + 1]) end;
                self.top_of_stack -= 1
                self.data_memory[self.top_of_stack] = bool(self.data_memory[self.top_of_stack] <= self.data_memory[self.top_of_stack+1])
                pass
            pass
        elif(function == "lod"):
            # lod: begin t := t + 1; s[t] := s[base(l) + a] end;
            # DEFAULT_INSTRUCTION
            self.top_of_stack +=1
            self.data_memory[self.top_of_stack] = self.data_memory[self.base(level) + constant]
            pass
        elif(function == "sto"):
            self.data_memory[self.base(level) + constant] = self.data_memory[self.top_of_stack]
            print(self.data_memory[self.top_of_stack], end ="\n")
            self.top_of_stack -= 1
            pass
        elif(function == "cal"):
            self.data_memory[self.top_of_stack + 1] = self.base(level)
            self.data_memory[self.top_of_stack + 2] = self.base_pointer
            self.data_memory[self.top_of_stack + 3] = self.program_counter
            self.base_pointer = self.top_of_stack +1 
            self.program_counter = constant
            pass
        elif(function == "int"):
            self.top_of_stack += constant
            pass
        elif(function == "jmp"):
            self.program_counter = constant
            pass
        elif(function == "jpc"):
            if (self.data_memory[self.top_of_stack] == 0):
                self.program_counter = constant
                self.top_of_stack -= 1

    # TODO: ------------------------
    
    def execute(self):
        """Execute the entire program in the instruction memory."""
        for index, value in enumerate(self.instruction_memory):
            self.program_counter += 1
            # (0, 0, 0)
            # F L C
            self.step(value[0], value[2], value[1])

    # TODO: ------------------------

if (__name__ == "__main__"):
    x = PCodeMachineEmulator()
    x.dump()
