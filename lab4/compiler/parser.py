"""A Recursive Descent Parser."""

from lexer import get_token, TokenType


# -----------------------------------------------------------------------------
# Parser Grammar
# -----------------------------------------------------------------------------
# ArithExpr           = AdditionExpr
# AdditionExpr        = MultiplicationExpr {AddOp MultiplicationExpr}
# MultiplicationExpr  = ExponentialExpr {MulOp ExponentialExpr}
# ExponentialExpr     = Term {ExpOp ExponentialExpr}
# Term                = Literal | '(' ArithExpr ')'
# Literal             = Identifier | Number


# -----------------------------------------------------------------------------
# Lexical Analyzer
# -----------------------------------------------------------------------------
# Number              = Digit { Digit }
# Identifier          = Letter { Letter | Digit }
# Operator            = '+' | '-' | '*' | '/' | '%' | '^'
# LeftParen           = '('
# RightParen          = ')'

def literal(text: str, pos: int) -> int:
    """Process literal.
    
    Literal ::= Identifier | Number
    
    """
    token, pos = get_token(text, pos)
    if token.token_type == TokenType.IDENTIFIER:
        pass
        # ...
    elif token.token_type == TokenType.NUMBER:
        pass
        # ...
    else:   # Error 
        pass
        # ...
    return pos
    

def term(text: str, pos: int) -> int:
    """Process term.
    
    Term ::= Literal | '(' ArithExpr ')'
    
    """
    token, new_pos = get_token(text, pos)
    # Literal
    if token.token_type == TokenType.IDENTIFIER:
        ...
    elif token.token_type == TokenType.NUMBER:
        ...
    # '(' ArithExpr ')'
    elif token.token_type == TokenType.LEFT_PAREN:
        match(token, TokenType.LEFT_PAREN)
        arith_expr(text, pos)
        match(token, TokenType.RIGHT_PAREN)
    else:   # Error
        raise
    
    return new_pos # pos -> new_pos
    

def expon_expr(text: str, pos: int) -> int:
    """Process ExponentialExpr.
    
    
    ExponentialExpr ::= Term {ExpOp ExponentialExpr}
    
    """
    term(text, pos)
    token, pos = get_token(text, pos)
    # NOTE: right to left if follow by power op
    while token.token_type == TokenType.POWER_OP:
        match(token, TokenType.POWER_OP)
        expon_expr(text, pos)
    
    return pos - len(token.lexeme)


def mul_expr(text: str, pos: int) -> int:
    """Process MultiplicationExpr.
    
    MultiplicationExpr ::= ExponentialExpr {MulOp ExponentialExpr}
    
    """
    expon_expr(text, pos)
    token, pos = get_token(text, pos)
    while token.token_type == TokenType.MUL_OP:
        match(token, TokenType.MUL_OP)
        expon_expr(text, pos)
    
    return pos - len(token.lexeme)

# TODO:------------------------------------------------------------------------------------

def add_expr(text: str, pos: int) -> int:
    """Process AdditionExpr.
    
    AdditionExpr ::= MultiplicationExpr {AddOp MultiplicationExpr}
    
    """
    mul_expr(text, pos)
    token, pos = get_token(text, pos)
    while token.token_type == TokenType.ADD_OP:
        match(token, TokenType.ADD_OP)
        mul_expr(text, pos)
    
    return pos - len(token.lexeme)

# TODO:------------------------------------------------------------------------------------

def arith_expr(text: str, pos: int = 0) -> int:
    """Process ArithExpr.
    
    ArithExpr   ::= AdditionExpr
    
    """
    add_expr(text, pos)
    # token, pos = get_token(text, pos)
    # while token.token_type == TokenType.ADD_OP:
    #     match(token, TokenType.ADD_OP)
    #     mul_expr(text, pos)
    
    return pos


if(__name__ == "__main__"):
    result = arith_expr("123")

    print(result)