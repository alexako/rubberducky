#RubberDucky
A simple programming language

"Sometimes, you just have to talk a problem out. I used to go to my boss and talk about something and he'd listen and then I'd just answer my own question and walk out without him saying a thing. I read about someone that put a rubber duck on their monitor so they could talk to it, so rubberducking is talking your way through a problem." - Jeff Atwood
[Coding Horror](https://blog.codinghorror.com/rubber-duck-problem-solving/)

CS145/AC2 - Alex Reyes

###Grammar Definition
```
<stmt_list> := <statement> { <statement> }
<statement> := <simple_stmt> | <compound_stmt> "."

<simple_stmt> := <vardecl> | <assign> | <print_stmt>
<vardecl> := "var" <vardecl_list>
          | "var" <vardecl_list> "=" <expr>
<vardecl_list> := <id> { "," <id> }
<id> := <letter> { <idchar> }
<idchar> := <letter> | <number> | "_"
<assign> := <id> = <expr>
<expr> := <id> ("+" | "-" | "*" | "/") <expr>
        | '('<expr>')'
        | <id>
        | <bool>

//Temp note
expr := term ((PLUS | MIUS) term)*
term := factor ((MUL | DIV) factor)*
factor := INTEGER | LPAREN expr RPAREN

<compound_stmt> := <if_stmt> | <for_loop> | <while_loop>
<if_stmt> := "if" '('<logic_expr>')' then '{'<stmt_list>'}'
              { "else if" '('<logic_expr>')' "then" '{'<stmt_list>'}' }
              { "else" '{'<stmt_list>'}' }
<logic_expr> := <expr> {<comp_op> (<expr> | <number>)}

<list> := '['<expr> { "," <expr> } | "" ']'
<for_loop> := "for" '('<id> "in" <list> ')' "do" '{'<stmt_list>'}'
<while_loop> := "while" '('<logic_expr>')' "do" '{'<stmt_list>'}'

<print_stmt> := "quack"'('<expr>')'
<break_stmt> := "break"

<comp_op> := '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not' 'in'|'is'|'is' 'not'
<bool> := "True" | "False"
<letter> := "A" | "B" | "C" | ... | "X" | "Y" | "Z"
          | "a" | "b" | "c" | ... | "x" | "y" | "z"
<number> := "0" | "1" | "2" | "3" | ... | "8" | "9"
```
