import sys
from antlr4 import *
from grammarALexer import grammarALexer
from grammarAParser import grammarAParser
from grammarAVisitor import grammarAVisitor
from functools import reduce
import z3
import re


op_reverse_dict={'==':'!=','>':'<=','<':'>=','!=':'==','>=':'<','<=':'>'}

class baseVisitor(grammarAVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.paths = []
        self.var_dict = {}
        self.stack=[]
    def initial_test_case(self,**dict):
        self.var_dict = dict
 
    def visitR(self, ctx: grammarAParser.RContext):
        for assign in ctx.assign_s():
            self.visitAssign_s(assign)
        print(self.var_dict)
        self.visitIfb(ctx.ifb(), "")

    def visitIfb(self, ctx: grammarAParser.IfbContext, cur):
        self.visitCondition(ctx.condition(), ctx.ifbs(),cur)
        self.visitThen(ctx.then(), cur)

    def visitIfbs(self, ctx: grammarAParser.IfbsContext, cur):
        # print(cur, type(ctx))
        if ctx:
            for c in ctx.ifb():
                self.visitIfb(c, cur)
        else:
            self.paths.append(cur)

    def visitThen(self, ctx: grammarAParser.ThenContext, cur):
        if not ctx:
            return
        self.visitEi(ctx.ei(), cur)
        if ctx.ELSE():
            new_cur = self.reverse_expr(self.stack.pop())
            # print(self.stack)
            self.stack.append(new_cur)
            # print(self.stack)
            self.visitIfbs(ctx.ifbs(), cur+new_cur+"->")
            self.stack.pop()
        else:
            self.stack.pop()

    def visitEi(self, ctx: grammarAParser.EiContext, cur):
        cur_condition=self.reverse_expr(self.stack[-1])
        for c in ctx.condition():
            self.visitCondition(c, ctx.ifbs(), cur)

    def visitCondition(
            self,
            ctx: grammarAParser.ConditionContext,
            s_ctx: grammarAParser.IfbsContext,
            cur):
        id_name = ctx.id1().getText()
        op = ctx.jop().getText()
        num = self.visitNum(ctx.num())
        cur = cur + (str(id_name) + " " + str(op) + " " + str(num) + "->")
        self.stack.append(str(id_name) + " " + str(op) + " " + str(num))
        # print(self.stack)
        if self.check(str(id_name),str(op),str(num)):
            self.visitIfbs(s_ctx, cur)

    def visitAssign_s(self, ctx: grammarAParser.Assign_sContext):
        id_name = ctx.id1().getText()
        num = self.visitNum(ctx.num())
        self.var_dict[id_name] = str(num)
    
    def visitNum(self, ctx: grammarAParser.NumContext):
        if ctx.MINUS():
            return str("-")+str(ctx.Digit())
        return str(ctx.Digit())
    
    def check(self, id_name, op, num):
        if id_name not in self.var_dict:
            return True
        var = int(self.var_dict[id_name])
        if op == "==":
            return var == int(num)
        if op == "!=":
            return var != int(num)
        if op == ">=":
            return var >= int(num)
        if op == "<=":
            return var <= int(num)
        if op == ">":
            return var > int(num)
        if op == "<":
            return var < int(num)

    def reverse_expr(self, expr):
        tmp_arr = expr.split()
        tmp_arr[1] = op_reverse_dict[tmp_arr[1]]
        return " ".join(tmp_arr)

    def combine_expr(self,s1,s2):
        s1_arr = s1.split()
        s2_arr = s2.split()







# with open("input.txt") as f:
#     input_arr = f.readlines()

input = FileStream("input.txt")
print(input)
lexer = grammarALexer(input)
stream = CommonTokenStream(lexer)
parser = grammarAParser(stream)
tree = parser.r()
print(tree.toStringTree(recog=parser))

visitor = baseVisitor()
visitor.visit(tree)
print(visitor.paths)
test_paths = visitor.paths


with open("result.csv","w") as f:
    id2z3 = {}
    for path in visitor.paths:
        exprs = path[:-2].split("->")
        z3_t_statements = []
        for expr in exprs:
            Id, op, num = expr.split()
            if Id not in id2z3:
                id2z3[Id] = z3.Int(Id)
            z3_var = id2z3[Id]
            if op == "==":
                z3_t_statement = z3_var == int(num)
            if op == "!=":
                z3_t_statement = z3_var != int(num)
            if op == ">=":
                z3_t_statement = z3_var >= int(num)
            if op == "<=":
                z3_t_statement = z3_var <= int(num)
            if op == ">":
                z3_t_statement = z3_var > int(num)
            if op == "<":
                z3_t_statement = z3_var < int(num)
            z3_t_statements.append(z3_t_statement)
        s = z3.Solver()
        s.add(reduce(z3.And, z3_t_statements))
        s.check()
        true_res = repr(s.model())
        print(true_res)
        f.write(path[:-2]+","+true_res+"\n")
    
