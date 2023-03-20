from enum import Enum
from typing import NamedTuple


"""
ACCEPT
    -  [<NUMBER>]  => [222] [3254]
    -  <OPERATOR>[<NUMBER>]  => +[222] -[3254]
"""




# class State(Enum):
#     Epsilon = "Epsilon"
#     RightParenthesis = "RightParenthesis"
#     LeftParenthesis = "LeftParenthesis"
#     NumberNone = "NumberNone"
#     NumberLeftParenthesis = "NumberLeftParenthesis"
#     Letter = "Letter"
#     OperatorNone = "OperatorNone"
#     OperatorLeftParenthesis = "OperatorLeftParenthesis"
#     Error = "Error"

# class Token(Enum):
#     Epsilon = "Epsilon"
#     Number = "Number"
#     Letter = "Letter"
#     Operator = "Operator"
#     Error = "Error"

# -----------------------------------------------------------------------------
class TokenType(Enum):
    """The token type."""
    # UNKNOWN = 0
    # END_OF_TEXT = 1
    # NUMBER = 2
    # IDENTIFIER = 3
    # ADD_OP = 4
    # MUL_OP = 5
    # POWER_OP = 6
    # LEFT_PAREN = 7
    # RIGHT_PAREN = 8




    Epsilon = 0
    RightParenthesis = 1
    LeftParenthesis = 2

    NumberNone = 3
    NumberLeftParenthesis = 4

    IDENTIFIER = 5

    OperatorNone = 6
    OperatorLeftParenthesis = 7

    END_OF_TEXT = 8
    Error = 9


# -----------------------------------------------------------------------------
class Token(NamedTuple):
    """The token class."""
    token_type: TokenType = TokenType.Epsilon
    lexeme: str = ""



def isDigit(symbol):
    return symbol in "0123456789"

def isLetter(symbol):
    return symbol.isalpha()

def isOperator(symbol):
    return symbol in "+-*%@="

def isWhiteSpace(symbol):
    return symbol in " "

def isLeftParenthesis(symbol):
    return symbol in "["

def isRightParenthesis(symbol):
    return symbol in "]"


def token(state, lexeme):
    return [state, lexeme]

# state = State.Epsilon
# lexeme = ""

def lexical_analyze(char, token: Token(TokenType.Epsilon, "")) -> Token:
    # global state
    # global lexeme

    symbol = char


    if (token.token_type == TokenType.Epsilon):
        if isDigit(symbol):
            # state = State.NumberNone
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.NumberNone

            lexeme = token.lexeme + symbol
            token = Token(TokenType.NumberNone, lexeme)
        elif isLetter(symbol):
            # state = State.Letter
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.IDENTIFIER

            lexeme = token.lexeme + symbol
            token = Token(TokenType.IDENTIFIER, lexeme)
        elif isOperator(symbol):
            # state = State.OperatorNone
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.OperatorNone

            lexeme = token.lexeme + symbol
            token = Token(TokenType.OperatorNone, lexeme)
        elif isLeftParenthesis(symbol):
            # state = State.LeftParenthesis
            # lexeme+=symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.LeftParenthesis

            lexeme = token.lexeme + symbol
            token = Token(TokenType.LeftParenthesis, lexeme)
        elif isWhiteSpace(symbol):
            # return token(State.Epsilon, lexeme)
            # token.lexeme += symbol
            # token.token_type = TokenType.END_OF_TEXT

            lexeme = token.lexeme
            token = Token(TokenType.END_OF_TEXT, lexeme)
        else:
            # state = State.Error
            raise
    
    elif (token.token_type == TokenType.NumberNone):
        if isDigit(symbol):
            # state = State.NumberNone
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.NumberNone

            lexeme = token.lexeme + symbol
            token = Token(TokenType.NumberNone, lexeme)
        elif isOperator(symbol):
            # state = State.OperatorNone
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.OperatorNone

            lexeme = token.lexeme + symbol
            token = Token(TokenType.OperatorNone, lexeme)
        elif isWhiteSpace(symbol):
            # return token(State.NumberNone, lexeme)
            # token.lexeme += symbol
            # token.token_type = TokenType.END_OF_TEXT

            lexeme = token.lexeme
            token = Token(TokenType.END_OF_TEXT, lexeme)
        else:
            # state = State.Error
            raise

    elif (token.token_type == TokenType.IDENTIFIER):
        if isLetter(symbol):
            # state = State.Letter
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.IDENTIFIER
            lexeme = token.lexeme + symbol
            token = Token(TokenType.IDENTIFIER, lexeme)
        elif isWhiteSpace(symbol):
            # return token(State.Letter, lexeme)
                        # token.lexeme += symbol

            lexeme = token.lexeme 
            token = Token(TokenType.END_OF_TEXT, lexeme)
        else:
            # state = State.Error
            raise

    elif (token.token_type == TokenType.OperatorNone):
        if isDigit(symbol):
            # state = State.NumberNone
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.NumberNone

            lexeme = token.lexeme + symbol
            token = Token(TokenType.NumberNone, lexeme)

        elif isLeftParenthesis(symbol):
            # state = State.LeftParenthesis
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.LeftParenthesis

            lexeme = token.lexeme + symbol
            token = Token(TokenType.LeftParenthesis, lexeme)
        elif isWhiteSpace(symbol):
            # return token(State.OperatorNone, lexeme)
                        # token.lexeme += symbol
            # token.token_type = TokenType.END_OF_TEXT

            lexeme = token.lexeme
            token = Token(TokenType.END_OF_TEXT, lexeme)
        else:
            # state = State.Error
            raise

    elif ( token.token_type == TokenType.LeftParenthesis):
        if isDigit(symbol):
            # state = State.NumberLeftParenthesis
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.NumberLeftParenthesis

            lexeme = token.lexeme + symbol
            token = Token(TokenType.NumberLeftParenthesis, lexeme)
        else:
            # state = State.Error
            raise

    elif (token.token_type == TokenType.NumberLeftParenthesis):
        if isDigit(symbol):
            # token.lexeme += symbol
            # token.token_type = TokenType.NumberLeftParenthesis

            lexeme = token.lexeme + symbol
            token = Token(TokenType.NumberLeftParenthesis, lexeme)
        elif isOperator(symbol):
            # state = State.OperatorLeftParenthesis
            # lexeme += symbol
            # token.lexeme += symbol
            # token.token_type = TokenType.OperatorLeftParenthesis

            lexeme = token.lexeme + symbol
            token = Token(TokenType.OperatorLeftParenthesis, lexeme)
        elif isRightParenthesis(symbol):
            # state = State.RightParenthesis
            # lexeme += symbol
            lexeme = token.lexeme + symbol
            token = Token(TokenType.RightParenthesis, lexeme)
            
        else:
            # state = State.Error
            raise

    elif (token.token_type == TokenType.OperatorLeftParenthesis):
        if isDigit(symbol):
            # state = State.NumberLeftParenthesis
            # lexeme += symbol
            lexeme = token.lexeme + symbol
            token = Token(TokenType.NumberLeftParenthesis, lexeme)
        else:
            # state = State.Error
            raise

    elif (token.token_type == TokenType.RightParenthesis):
        if isOperator(symbol):
            # state = State.OperatorNone
            # lexeme += symbol
            lexeme = token.lexeme + symbol
            token = Token(TokenType.OperatorNone, lexeme)
        elif isWhiteSpace(symbol):
            # return token(State.RightParenthesis, lexeme)
            # state = State.Epsilon
            # lexeme += symbol
            # token.token_type = TokenType.END_OF_TEXT
            lexeme = token.lexeme
            token = Token(TokenType.END_OF_TEXT, lexeme)
        else:
            # state = State.Error
            raise

    else:
        # return token(State.Error, "")
        raise

    return token






if (__name__ == "__main__"):
    text = "1 + 2345 * - * 123+234 + 9 +[234] [33456+32] "

    result = []

    for word in text.split(" "):
        print(word)
        # separate input to char
        token = Token(TokenType.Epsilon, "")
        for char in word:
            token = lexical_analyze(char, token)

        result.append(token)
        print()
        print(result)

    # result
    for _ in result:
        print(_)

