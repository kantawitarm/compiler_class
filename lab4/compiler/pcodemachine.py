"""The P-code machine module."""


# -----------------------------------------------------------------------------
DEFAULT_INSTRUCTION = 0
DEFAULT_INSTRUCTION_MEMORY_SIZE = 200

DEFAULT_DATA = 0
DEFAULT_DATA_MEMORY_SIZE = 500

DEFAULT_REGISTER = 0


# -----------------------------------------------------------------------------
class PCodeMachineEmulator:
    """The P-code machine emulator."""

    def __init__(self):
        """Construct a P-code machine emulator."""
        # Memory
        self.instruction_memory = \
            [DEFAULT_INSTRUCTION]*DEFAULT_INSTRUCTION_MEMORY_SIZE
        self.data_memory = [DEFAULT_DATA]*DEFAULT_DATA_MEMORY_SIZE

        # Registers
        self.program_counter = DEFAULT_REGISTER
        self.base_pointer = DEFAULT_REGISTER
        self.top_of_stack = DEFAULT_REGISTER

    def dump(self):
        """Dump the machine contents."""
        return ""

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
