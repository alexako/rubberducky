#RubberDucky
A simple programming language


CS145/AC2 - Alex Reyes

###Grammar Definition
```
//Variable declaration
<vardecl> -> var <vardecllist> .
          | var <vardecllist> = <expr> .
<vardecllist> -> <id> { , <id> }
<id> -> <letter> { <idchar> }
<idchar> -> <letter> | <digit> | _

//Variable assignment
<assign> -> <id> = <expr> .
<expr> -> <id> + <expr>
        | <id> - <expr>
        | <id> * <expr>
        | <id> / <expr>
        | (<expr>)
        | <id>
```
