import re

# Define token patterns using regular expressions
token_patterns = [
    ('NUMBER', r'\d+'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('WHITESPACE', r'\s+')
]

# Tokenize input code
def tokenize(code):
    tokens = []
    while code:
        match = None
        for token_type, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append((token_type, value))
                break
        if not match:
            raise ValueError('Invalid input:', code)
        code = code[len(match.group(0)):]
    return tokens

# Example usage
code = "3 + 4 * (5 - 2)"
tokens = tokenize(code)
print(tokens)
