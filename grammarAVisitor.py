# Generated from .\grammarA.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammarAParser import grammarAParser
else:
    from grammarAParser import grammarAParser

# This class defines a complete generic visitor for a parse tree produced by grammarAParser.

class grammarAVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammarAParser#r.
    def visitR(self, ctx:grammarAParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarAParser#ifb.
    def visitIfb(self, ctx:grammarAParser.IfbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarAParser#then.
    def visitThen(self, ctx:grammarAParser.ThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarAParser#ei.
    def visitEi(self, ctx:grammarAParser.EiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarAParser#condition.
    def visitCondition(self, ctx:grammarAParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarAParser#jop.
    def visitJop(self, ctx:grammarAParser.JopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarAParser#id1.
    def visitId1(self, ctx:grammarAParser.Id1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarAParser#ifbs.
    def visitIfbs(self, ctx:grammarAParser.IfbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarAParser#assign_s.
    def visitAssign_s(self, ctx:grammarAParser.Assign_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarAParser#num.
    def visitNum(self, ctx:grammarAParser.NumContext):
        return self.visitChildren(ctx)



del grammarAParser