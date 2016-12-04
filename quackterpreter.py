#quack => keyword for print
#squeeze => keyword for user input


#
# Lexer
#

#Token types
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF'
)

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str_(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid syntax found")

    def next_pos(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.next_pos()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.next_pos()
        return int(result)

    def get_next_token(self):
        """
            Lexical Analyzer
        """

        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.next_pos()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.next_pos()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.next_pos()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.next_pos()
                return Token(DIV, '/')

            if self.current_char == '(':
                self.next_pos()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.next_pos()
                return Token(RPAREN, ')')

            self.error()

        return Token(EOF, None)

#
# Parser
#

class AST(object):
    """ Abstract Syntax Tree Super class """
    pass

class BinaryOper(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class UnaryOper(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax found")

    def eat(self, token_type):
        """
            Checks if the current token type matches the passed token type
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """ Non-terminal method """
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOper(token, self.factor())
            return node
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOper(token, self.factor())
            return node
        elif token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

    def term(self):
        """ Non-terminal method """
        node = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            #TODO: Clean this up
            node = BinaryOper(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
            Parser
            Non-terminal method
        """

        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinaryOper(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()

#
# Interpreter
#
class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Quackterpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinaryOper(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_UnaryOper(self, node):
        op = node.op.type
        if op == PLUS:
            return +self.visit(node.expr)
        elif op == MINUS:
            return -self.visit(node.expr)

    def visit_Num(self, node):
        return node.value

    def quackterpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

def show_help():
    print """
    Welcome to RubberDucky v1.0!

    RubberDucky is a simple interpreter built entirely in Python. The keywords
    and syntax can be seen below. This is a project for CS145. Research
    resources, source code, and the README file can be seen in my repository on
    Github at https://github.com/alexako/rubberducky.

    Syntax:
    Example:
    """

def goodbye_msg():
    print "---------------------"
    print "Bye, bye RubberDucky!"
    print "---------------------"

def main():
    print "RubberDucky v1.0 [2016-12-3] - Alex Reyes"
    print "Type 'help' for more information"
    print "-----------------------------------------"

    output_line_counter = 0

    while True:
        try:
            text = raw_input('ducky>> ')
        except EOFError:
            break

        if text == "help":
            show_help()
            continue
        if text == "exit" or text == "quit":
            goodbye_msg()
            exit()
        if not text:
            continue

        output_line_counter += 1
        try:
            lexer = Lexer(text)
            parser = Parser(lexer)
            quackterpreter = Quackterpreter(parser)
            result = quackterpreter.quackterpret()
        except:
            print "SyntaxError: Invalid syntax"
            continue

        print "output[%d]:\n %s" % (output_line_counter, result)

if __name__ == '__main__':

    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            text = f.read()

        try:
            lexer = Lexer(text)
            parser = Parser(lexer)
            quackterpreter = Quackterpreter(parser)
            result = quackterpreter.quackterpret()
        except:
            print "SyntaxError: Invalid syntax"
            
        print result
    else:
        main()
