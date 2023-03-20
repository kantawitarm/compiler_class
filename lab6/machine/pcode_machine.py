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

    def load_program(self, list_of_pcode: list):
        """Load program into instruction memory."""
        if len(list_of_pcode) > len(self.instruction_memory):
            raise ValueError("Too many instructions to be held in the memory.")

        for index, value in enumerate(list_of_pcode):
            self.instruction_memory[index] = value

    def step(self):
        """Execute one instruction."""

    def execute(self):
        """Execute the entire program in the instruction memory."""


if (__name__ == "__main__"):
    x = PCodeMachineEmulator()
    x.dump()
