#RubberDucky
A simple programming language

"Sometimes, you just have to talk a problem out. I used to go to my boss and talk about something and he'd listen and then I'd just answer my own question and walk out without him saying a thing. I read about someone that put a rubber duck on their monitor so they could talk to it, so rubberducking is talking your way through a problem." - Jeff Atwood
[Coding Horror](https://blog.codinghorror.com/rubber-duck-problem-solving/)

CS145/AC2 - Alex Reyes

###Grammar Definition
```
//Variable declaration
<vardecl> := var <vardecllist> .
          | var <vardecllist> = <expr> .
<vardecllist> := <id> { , <id> }
<id> := <letter> { <idchar> }
<idchar> := <letter> | <digit> | _

//Variable assignment
<assign> := <id> = <expr> .
<expr> := <id> + <expr>
        | <id> - <expr>
        | <id> * <expr>
        | <id> / <expr>
        | (<expr>)
        | <id>
```
