"""Test cases for P-code machine emulator."""
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append('../../')


from machine.pcode_machine import PCodeMachineEmulator
from machine.pcode_machine import DEFAULT_INSTRUCTION
from machine.pcode_machine import DEFAULT_INSTRUCTION_MEMORY_SIZE
from machine.pcode_machine import DEFAULT_DATA
from machine.pcode_machine import DEFAULT_DATA_MEMORY_SIZE
from machine.pcode_machine import DEFAULT_REGISTER


# -----------------------------------------------------------------------------
def test_constructor():
    """Construct a P-code machine emulator."""
    # Arrange
    # Act
    machine = PCodeMachineEmulator()

    # Assert
    assert machine is not None

    # instruction memory
    assert machine.instruction_memory is not None
    assert len(machine.instruction_memory) == DEFAULT_INSTRUCTION_MEMORY_SIZE
    for index in range(DEFAULT_INSTRUCTION_MEMORY_SIZE):
        assert machine.instruction_memory[index] == DEFAULT_INSTRUCTION

    # # data memory
    assert machine.data_memory is not None
    assert len(machine.data_memory) == DEFAULT_DATA_MEMORY_SIZE
    for index in range(DEFAULT_DATA_MEMORY_SIZE):
        assert machine.data_memory[index] == DEFAULT_DATA

    # # registers
    assert machine.program_counter is not None
    assert machine.program_counter == DEFAULT_REGISTER

    assert machine.base_pointer is not None
    assert machine.base_pointer == DEFAULT_REGISTER

    assert machine.top_of_stack is not None
    assert machine.top_of_stack == DEFAULT_REGISTER


# -----------------------------------------------------------------------------
def test_dump():
    """Dump the machine state."""
    # Arrange
    machine = PCodeMachineEmulator()
    expected = \
        "P-Code Machine\n"          \
        "Registers\n"               \
        "Program counter:   0\n"    \
        "Base pointer:      0\n"    \
        "Top of stack:      0\n"    \
        "\n"                        \
        "Instruction memory\n"
    for _ in range(DEFAULT_INSTRUCTION_MEMORY_SIZE // 10):
        expected = expected +   \
            "(0, 0, 0) (0, 0, 0) (0, 0, 0) (0, 0, 0) (0, 0, 0)"  \
            " (0, 0, 0) (0, 0, 0) (0, 0, 0) (0, 0, 0) (0, 0, 0)\n"
    expected = expected + "\n"

    data = ""
    data = data + "Data memory\n"
    for _ in range(DEFAULT_DATA_MEMORY_SIZE // 10):
        data = data + f"{hex(0x0)} {hex(0x0)} {hex(0x0)} {hex(0x0)} {hex(0x0)} {hex(0x0)} {hex(0x0)} {hex(0x0)} {hex(0x0)} {hex(0x0)}\n"

    # print(_)

    # print(data)
    # Act
    text = machine.dump()

    # Assert
    assert text == expected

# test_dump()

# -----------------------------------------------------------------------------
def test_load_program():
    """Load program into the p-code machine."""


# -----------------------------------------------------------------------------
def test_step():
    """Execute one instruction in the p-code machine's instruction memory."""


# -----------------------------------------------------------------------------
def test_execulte():
    """Execute the entire program."""
