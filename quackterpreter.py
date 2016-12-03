#quack => keyword for print
#squeeze => keyword for user input

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


class Quackterpreter(object):
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
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result

    def term(self):
        """ Non-terminal method """
        result = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.factor()

        return result

    def expr(self):
        """
            Parser
            Non-terminal method
        """

        result = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        return result

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

def main():
    output_line_counter = 0
    while True:
        try:
            text = raw_input('ducky>> ')
            if text == "help":
                show_help()
                continue
            if text == "exit" or text == "quit":
                print "---------------------"
                print "Bye, bye RubberDucky!"
                print "---------------------"
                exit()
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Quackterpreter(lexer)
        result = interpreter.expr()
        output_line_counter += 1
        print "output[%d]:\n %s" % (output_line_counter, result)

if __name__ == '__main__':
    print "RubberDucky v1.0 [2016-12-3] - Alex Reyes"
    print "Type 'help' for more information"
    print "-----------------------------------------"

    main()
