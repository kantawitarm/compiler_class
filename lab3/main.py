from typing import NamedTuple
from enum import Enum
import pytest

# -----------------------------------------------------------------------------
ADD_OPERATOR = "+-"
# MULTIPLY_OPERATOR = "*/%"
# POWER_OPERATOR = "^"
# ALL_OPERATOR = ADD_OPERATOR + MULTIPLY_OPERATOR + POWER_OPERATOR

ALL_OPERATOR = ADD_OPERATOR


# -----------------------------------------------------------------------------
class TokenType(Enum):
    """The token type."""
    UNKNOWN = 0
    END_OF_TEXT = 1
    NUMBER = 2
    IDENTIFIER = 3
    # ADD_OP = 4
    # MUL_OP = 5
    # POWER_OP = 6
    # LEFT_PAREN = 7
    # RIGHT_PAREN = 8
    

# -----------------------------------------------------------------------------
class Token(NamedTuple):
    """The token class."""
    token_type: TokenType = TokenType.UNKNOWN
    lexeme: str = ""


def main(input: list):
    for _token in input:
        if(_token.token_type != TokenType.NUMBER):
            raise ValueError(f"[Syntax Analysis]\t -{_token.lexeme}- is not a number.")
    return input



if (__name__ == "__main__"):
    x = main([ Token(TokenType.NUMBER, "22")])
    print(x)


