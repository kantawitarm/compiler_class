from typing import NamedTuple
from enum import Enum


# -----------------------------------------------------------------------------
class TokenType(Enum):
    """The token type."""
    UNKNOWN = 0
    END_OF_TEXT = 1
    NUMBER = 2
    IDENTIFIER = 3
    ADD_OP = 4
    MUL_OP = 5
    POWER_OP = 6
    LEFT_PAREN = 7
    RIGHT_PAREN = 8
    

# -----------------------------------------------------------------------------
class Token(NamedTuple):
    """The token class."""
    token_type: TokenType = TokenType.UNKNOWN
    lexeme: str = ""
