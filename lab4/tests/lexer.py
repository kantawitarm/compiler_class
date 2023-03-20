import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append('../')

import pytest

# from lab4 import main
from lexer import get_token, TokenType, Token
"""Test cases for lexical analyzer."""

# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, expected",
    [
        ("", (Token(TokenType.END_OF_TEXT, ""), 0)),
        ("   ", (Token(TokenType.END_OF_TEXT, ""), 3)),
        ("7", (Token(TokenType.NUMBER, "7"), 1)),
        ("487", (Token(TokenType.NUMBER, "487"), 3)),
        (" 456", (Token(TokenType.NUMBER, "456"), 4)),
        ("abc", (Token(TokenType.IDENTIFIER, "abc"), 3)),
        (" a24 ", (Token(TokenType.IDENTIFIER, "a24"), 4)),
        (" + ", (Token(TokenType.ADD_OP, "+"), 2)),
        ("\t/ ", (Token(TokenType.MUL_OP, "/"), 2)),
        # ("    ^ ", (Token(TokenType.POWER_OP, "^"), 5)),
    ]
)
def test_get_token(text, expected):
    """Get the next token from text starting from pos."""
    # Arrange
    # Act
    result = get_token(text)

    # Assert
    assert result == expected


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, list_of_token",
    [
        (
            "7 489 abc",
            [
                Token(TokenType.NUMBER, "7"),
                Token(TokenType.NUMBER, "489"),
                Token(TokenType.IDENTIFIER, "abc"),
            ]
        ),
        (
            "1 + 2 * 3",
            [
                Token(TokenType.NUMBER, "1"),
                Token(TokenType.ADD_OP, "+"),
                Token(TokenType.NUMBER, "2"),
                Token(TokenType.MUL_OP, "*"),
                Token(TokenType.NUMBER, "3"),
            ]
        ),
    ]
)
def test_get_list_of_token(text, list_of_token):
    """Get list of tokens."""
    # Arrange
    # Act
    token, pos = get_token(text)
    result = []
    while token.token_type != TokenType.END_OF_TEXT:
        result.append(token)
        token, pos = get_token(text, pos)

    # Assert
    assert result == list_of_token
    assert pos == len(text)
