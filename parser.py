# Recursive descent parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = 0

    def eat(self, token_type):
        if self.current_token[0] == token_type:
            self.token_index += 1
            if self.token_index < len(self.tokens):
                self.current_token = self.tokens[self.token_index]
            else:
                self.current_token = None
        else:
            raise SyntaxError('Invalid syntax')

    def factor(self):
        token = self.current_token
        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return int(token[1])
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            result = self.expr()
            self.eat('RPAREN')
            return result

    def term(self):
        result = self.factor()
        while self.current_token and self.current_token[0] in ('TIMES', 'DIVIDE'):
            token = self.current_token
            if token[0] == 'TIMES':
                self.eat('TIMES')
                result *= self.factor()
            elif token[0] == 'DIVIDE':
                self.eat('DIVIDE')
                result /= self.factor()
        return result

    def expr(self):
        result = self.term()
        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS'):
            token = self.current_token
            if token[0] == 'PLUS':
                self.eat('PLUS')
                result += self.term()
            elif token[0] == 'MINUS':
                self.eat('MINUS')
                result -= self.term()
        return result

# Example usage
parser = Parser(tokens)
result = parser.expr()
print(result)
