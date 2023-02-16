import pytest


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, list_of_token",
    [
      """  (
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
        """
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
