"""Code generator."""

class CodeGenerator:
    """The code generator."""


# -----------------------------------------------------------------------------
class PCodeAssemblyGenerator(CodeGenerator):
    """P-code assembly generator"""

    def gen_number(self, value):
        """Generate code for a number."""
        return "LIT 0 " + str(value)


# -----------------------------------------------------------------------------
class PCodeBinaryGenerator(CodeGenerator):
    """P-code binary generator"""

    def gen_number(self, value):
        """Generate code for a number."""
        return PCode(0, 0, int(value)).bytecode()


# -----------------------------------------------------------------------------
class X86AssemblyGenerator(CodeGenerator):
    """X86 assembly generator"""

    def gen_number(self, value):
        """Generate code for a number."""
        return "movl $" + str(value) + ", -4(%rbp)"
