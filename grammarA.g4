grammar grammarA;

options {
     language = Python3;
}
     

IF : 'if';
ELSE : 'else';

MINUS : '-' ;
LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ : '!=';

ASSIGN : '=' ;
SEMI : ';' ;
LPAREN : '(';
RPAREN : ')';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';

Digit : [0-9]+ ;
Alphabets : [a-z]+ ;

r : (assign_s)* ifb (assign_s)*;
ifb : IF LPAREN condition RPAREN OPEN_BRACE (assign_s)* (ifbs)? (assign_s)*CLOSE_BRACE (then)? ;
then : ei (ELSE OPEN_BRACE (assign_s)* (ifbs)? (assign_s)*CLOSE_BRACE)? ;
ei : (ELSE IF LPAREN condition RPAREN OPEN_BRACE (assign_s)* (ifbs)? (assign_s)*CLOSE_BRACE)* ;
condition : id1 jop num ;
jop : (EQUALS | NOT_EQ | LESS_THAN | GREATER_THAN | LT_EQ | GT_EQ) ;
id1 : (Alphabets)+ ;
ifbs : (ifb)+ ;
assign_s : id1 ASSIGN num SEMI ;
num : (MINUS)? Digit ;


WS : [ \t\r\n]+ -> skip;