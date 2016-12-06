#RubberDucky

RubberDucky is a dynamic, static typed programming language. It belongs to the procedural programming language paradigm. The user interface was built with a Python GUI framework called Kivy. Python must be installed in order to run.

####To run:
```
#Navigate to project directory
python main.py
```
####Compiler:
```
python quackterpreter.py example.ducky
```

####Interactive Interpreter:
RubberDucky can act as an interactive interpreter. Simple execute the `quackterpreter.py` without passing any arguments.

"Sometimes, you just have to talk a problem out. I used to go to my boss and talk about something and he'd listen and then I'd just answer my own question and walk out without him saying a thing. I read about someone that put a rubber duck on their monitor so they could talk to it, so rubberducking is talking your way through a problem." - Jeff Atwood
[Coding Horror](https://blog.codinghorror.com/rubber-duck-problem-solving/)

CS145/AC2 - Alex Reyes

###Sample Code
```Pascal
PROGRAM Example;
VAR
   number     : INTEGER;
   a, b, c, x : INTEGER;
   y          : REAL;

BEGIN {Example}
   BEGIN
      number := 2;
      a := number;
      b := 10 * a + 10 * number DIV 4;
      c := a - -b
   END;
   x := 11;
   y := 20 / 7 + 3.14;
   { This is a comment. }

END.  
```

###Grammar Definition
```
<stmt_list> := <statement> { <statement> }
<statement> := <simple_stmt> | <compound_stmt> PERIOD

<simple_stmt> := <vardecl> | <assign> | <print_stmt> | <list>
<vardecl> := VAR <vardecl_list>
          | VAR <vardecl_list> ASSIGN <expr>
<vardecl_list> := <id> { "," <id> }
<id> := <letter> { <idchar> }
<idchar> := <letter> | <number> | UNDERSCORE
<assign> := <id> ASSIGN <expr>
<expr> := term ((PLUS | MIUS) term)*
<term> := factor ((MUL | DIV) factor)*
<factor> := (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN

<compound_stmt> := <if_stmt> | <for_loop> | <while_loop>
<if_stmt> := "if" <logic_expr> then LBRACE <stmt_list> RBRACE
              { "else if" <logic_expr> "then" LBRACE <stmt_list> RBRACE }
              { "else" LBRACE <stmt_list> RBRACE }
<logic_expr> := <expr> {<comp_op> (<expr> | <number>)}

<list> := LSQRBR <expr> { "," <expr> } | "" RSQRBR
<for_loop> := "for" <id> "in" <list> "do" LBRACE <stmt_list> RBRACE
<while_loop> := "while" <logic_expr> "do" LBRACE <stmt_list> RBRACE

<print_stmt> := "quack" <expr>
<break_stmt> := "break"

<comp_op> := '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not' 'in'|'is'|'is' 'not'
<bool> := "True" | "False"
<letter> := "A" | "B" | "C" | ... | "X" | "Y" | "Z"
          | "a" | "b" | "c" | ... | "x" | "y" | "z"
<number> := "0" | "1" | "2" | "3" | ... | "8" | "9"
```

Keywords:   
-`PROGRAM` - Indicates beginning of the program   
-`BEGIN` - Indicates the beginning of a block   
-`END` - Indicates the end of a block

####Sources:
Appel, Palsberg. "Modern Compiler Implementation in Java, Second Edition". 2002

Crenshaw, Jack W. Ph.D. "Let's Build A Compiler". July 24 1988  
http://compilers.iecc.com/crenshaw/

Mogensen, Torben. "Basics of Compiler Design". August 20, 2010  
http://www.diku.dk/~torbenm/Basics

"Syntax: Grammars, Derivations, Parse Trees". September 1st, 2010  
http://www.idi.ntnu.no/emner/tdt4165/handouts/03-handouts.pdf

Kivy API docs:  
https://kivy.org/docs/gettingstarted/intro.html

Python Grammar specifications:  
https://docs.python.org/2/reference/grammar.html
