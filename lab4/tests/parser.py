import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append('../../')

import pytest

# from lab4 import main
# from lab4.TEACHER_parser import arith_expr
"""Test cases for parser analyzer."""


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, expected",
    [
        ("123", 3)
    ]
)
def test_get_parser(text, expected):
    """Get the next token from text starting from pos."""
    # Arrange
    # Act
    result = arith_expr(text)
    print("result")
    print(result)
    # Assert
    # assert result == expected

test_get_parser("123", 1)





