"""Abstract Syntax Tree."""


# -----------------------------------------------------------------------------
class AbstractSyntaxTree:
    """The abstract syntax tree."""


# -----------------------------------------------------------------------------
class ArithExpr(AbstractSyntaxTree):
    """The Arithmetic Expression."""


# -----------------------------------------------------------------------------
class BinaryExpr(ArithExpr):
    """The Binary Expression."""

    def __init__(self, opr, left, right):
        """Construct an object."""
        self.opr = opr
        self.left = left
        self.right = right

    def __str__(self):
        """Return the string representation."""
        return "(" + str(self.left) + " " + self.opr + " " + \
            str(self.right) + ")"


# -----------------------------------------------------------------------------
class AdditionExpr(BinaryExpr):
    """The Addition Expression."""

    def evaluate(self):
        """Evaluate the expression."""
        if self.opr == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.opr == "-":
            return self.left.evaluate() - self.right.evaluate()
        else:
            raise ValueError(f"Unrecognized operator [{self.opr}]")


# -----------------------------------------------------------------------------
class MultiplicationExpr(BinaryExpr):
    """The Multiplication Expression."""


# -----------------------------------------------------------------------------
class ExponentialExpr(BinaryExpr):
    """The Exponential Expression."""


# -----------------------------------------------------------------------------
class Literal(ArithExpr):
    """The Literal."""


# -----------------------------------------------------------------------------
class Number(Literal):
    """The number."""

    def __init__(self, value):
        """Construct an object."""
        self.value = value

    def __str__(self):
        """Return string representation."""
        return str(self.value)

    def evaluate(self):
        """Evaluate the expression."""
        return int(self.value)

    def gen_code(self):
        """Generate target code."""
        # P-code assembly
        return "LIT 0 " + str(self.value)

        # P-code object code
        return PCode(0, 0, int(self.value)).bytecode()

        # x86 assembly
        return "movl $" + str(self.value) + ", -4(%rbp)"

    def gen_code2(self, targer_code_generator):
        """Generate target code."""
        # P-code assembly
        return targer_code_generator.gen_number(self.value)


# -----------------------------------------------------------------------------
class Identifier(Literal):
    """The identifier."""

    def __init__(self, name, value):
        """Construct an object."""
        self.name = name
        self.value = value

    def __str__(self):
        """Return string representation."""
        return str(self.name)

    def evaluate(self):
        """Evaluate the expression."""
        return int(self.value)

    def assign(self, value):
        """Assign the value to the identifier."""
        self.value = value
