from typing import NamedTuple
from enum import Enum


# -----------------------------------------------------------------------------
ADD_OPERATOR = "+-"
MULTIPLY_OPERATOR = "*/%"
POWER_OPERATOR = "^"
ALL_OPERATOR = ADD_OPERATOR + MULTIPLY_OPERATOR + POWER_OPERATOR


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


# -----------------------------------------------------------------------------
def skip_whitespace(text: str, pos: int) -> int:
    """Skip white spaces in text starting from pos.
    
    Args
    ----
        text:   the text to be scanned.
        pos:    the starting position to scan.
      
    Returns
    -------
        the position of the first non-whitespace starting from pos.
        
    """
    while pos < len(text) and text[pos].isspace():
        pos = pos + 1
    
    return pos
    
    
# -----------------------------------------------------------------------------
def get_number(text: str, pos: int = 0) -> tuple:
    """Get the number from text string starting at pos.
    
    Args
    ----
        text:       the text to be scanned.
        pos:        the starting position to scan.
        
    Returns
    -------
        number and the position after the token
    
    """
    cur_pos = pos
    while cur_pos < len(text) and text[cur_pos].isdigit():
        cur_pos = cur_pos + 1
    return text[pos:cur_pos], cur_pos
        
    
# -----------------------------------------------------------------------------
def get_identifier(text: str, pos: int = 0) -> tuple:
    """Get the identifier from text string starting at pos.
    
    Args
    ----
        text:       the text to be scanned.
        pos:        the starting position to scan.
        
    Returns
    -------
        identifier and the position after the token
    
    """
    cur_pos = pos
    while cur_pos < len(text) and text[cur_pos].isalnum():
        cur_pos = cur_pos + 1
    return text[pos:cur_pos], cur_pos
        
    

# -----------------------------------------------------------------------------
def get_symbol(text: str, pos: int = 0) -> tuple:
    """Get the symbol from text string starting at pos.
    
    Args
    ----
        text:       the text to be scanned.
        pos:        the starting position to scan.
        
    Returns
    -------
        symbol and the position after the token
    
    """
    cur_pos = pos
    while cur_pos < len(text) and text[cur_pos] in ALL_OPERATOR:
        cur_pos = cur_pos + 1
    return text[pos:cur_pos], cur_pos
        
    

# -----------------------------------------------------------------------------
def get_token(text: str, pos: int = 0) -> tuple:
    """Get the token from text string starting at pos.
    
    Args
    ----
        text:       the text to be scanned.
        pos:        the starting position to scan.
        
    Returns
    -------
        token and the position after the token
    
    """
    pos = skip_whitespace(text, pos)
    token = Token(TokenType.END_OF_TEXT, "")
    
    if pos < len(text):
        if text[pos].isdigit():
            lexeme, pos = get_number(text, pos)
            token = Token(TokenType.NUMBER, lexeme)
        elif text[pos].isalpha():
            lexeme, pos = get_identifier(text, pos)
            token = Token(TokenType.IDENTIFIER, lexeme)
        elif text[pos] in ADD_OPERATOR:
            if pos+1 < len(text) and text[pos + 1] == text[pos]:
                lexeme = text[pos:pos+2]
                token = Token(TokenType.INCREMENT, lexeme)
            else:
                lexeme, pos = get_symbol(text, pos)
                token = Token(TokenType.ADD_OP, lexeme)
        elif text[pos] in MULTIPLY_OPERATOR:
            lexeme, pos = get_symbol(text, pos)
            token = Token(TokenType.MUL_OP, lexeme)
        elif text[pos] == '(':
            lexeme, pos = get_symbol(text, pos)
            token = Token(TokenType.LEFT_PAREN, lexeme)
        elif text[pos] == ')':
            lexeme, pos = get_symbol(text, pos)
            token = Token(TokenType.RIGHT_PAREN, lexeme)
        else:
            raise ValueError(f"Unrecognized symbol [{text[pos]}]")
        
    return token, pos


def main(input: str):
    token, pos = get_token(input)
    result = []
    while token.token_type != TokenType.END_OF_TEXT:
        result.append(token)
        token, pos = get_token(input, pos)
    
    return result


if (__name__ == "__main__"):
    print (main("1212 jkbu 3231"))