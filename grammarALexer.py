# Generated from .\grammarA.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\6\21O\n\21\r\21\16\21P\3\22\6\22T\n\22\r\22\16\22")
        buf.write("U\3\23\6\23Y\n\23\r\23\16\23Z\3\23\3\23\2\2\24\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\3\2\5\3\2\62;\3\2c|\5\2\13\f")
        buf.write("\17\17\"\"\2`\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5*\3\2\2\2\7/\3\2\2")
        buf.write("\2\t\61\3\2\2\2\13\63\3\2\2\2\r\65\3\2\2\2\178\3\2\2\2")
        buf.write("\21;\3\2\2\2\23>\3\2\2\2\25A\3\2\2\2\27C\3\2\2\2\31E\3")
        buf.write("\2\2\2\33G\3\2\2\2\35I\3\2\2\2\37K\3\2\2\2!N\3\2\2\2#")
        buf.write("S\3\2\2\2%X\3\2\2\2\'(\7k\2\2()\7h\2\2)\4\3\2\2\2*+\7")
        buf.write("g\2\2+,\7n\2\2,-\7u\2\2-.\7g\2\2.\6\3\2\2\2/\60\7/\2\2")
        buf.write("\60\b\3\2\2\2\61\62\7>\2\2\62\n\3\2\2\2\63\64\7@\2\2\64")
        buf.write("\f\3\2\2\2\65\66\7?\2\2\66\67\7?\2\2\67\16\3\2\2\289\7")
        buf.write("@\2\29:\7?\2\2:\20\3\2\2\2;<\7>\2\2<=\7?\2\2=\22\3\2\2")
        buf.write("\2>?\7#\2\2?@\7?\2\2@\24\3\2\2\2AB\7?\2\2B\26\3\2\2\2")
        buf.write("CD\7=\2\2D\30\3\2\2\2EF\7*\2\2F\32\3\2\2\2GH\7+\2\2H\34")
        buf.write("\3\2\2\2IJ\7}\2\2J\36\3\2\2\2KL\7\177\2\2L \3\2\2\2MO")
        buf.write("\t\2\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\"\3")
        buf.write("\2\2\2RT\t\3\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2")
        buf.write("\2V$\3\2\2\2WY\t\4\2\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z")
        buf.write("[\3\2\2\2[\\\3\2\2\2\\]\b\23\2\2]&\3\2\2\2\6\2PUZ\3\b")
        buf.write("\2\2")
        return buf.getvalue()


class grammarALexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    MINUS = 3
    LESS_THAN = 4
    GREATER_THAN = 5
    EQUALS = 6
    GT_EQ = 7
    LT_EQ = 8
    NOT_EQ = 9
    ASSIGN = 10
    SEMI = 11
    LPAREN = 12
    RPAREN = 13
    OPEN_BRACE = 14
    CLOSE_BRACE = 15
    Digit = 16
    Alphabets = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'-'", "'<'", "'>'", "'=='", "'>='", "'<='", 
            "'!='", "'='", "';'", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "MINUS", "LESS_THAN", "GREATER_THAN", "EQUALS", 
            "GT_EQ", "LT_EQ", "NOT_EQ", "ASSIGN", "SEMI", "LPAREN", "RPAREN", 
            "OPEN_BRACE", "CLOSE_BRACE", "Digit", "Alphabets", "WS" ]

    ruleNames = [ "IF", "ELSE", "MINUS", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                  "GT_EQ", "LT_EQ", "NOT_EQ", "ASSIGN", "SEMI", "LPAREN", 
                  "RPAREN", "OPEN_BRACE", "CLOSE_BRACE", "Digit", "Alphabets", 
                  "WS" ]

    grammarFileName = "grammarA.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


