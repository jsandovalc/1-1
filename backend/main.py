import ast
from sanic import Sanic
from sanic.response import json, file

app = Sanic()

app.static('/static', './dist/static')

@app.route('/')
async def index(request):
    return await file('dist/index.html')

@app.route('/eval', methods=['POST'])
async def parse(request):
    """Parse expression, return eval(expr).

    Request must include `expr` and `table`.

    """
    return json({'result': eval(request.json['expr'],
                                request.json['table'])})



class PolishNotationVisitor(ast.NodeVisitor):
    def __init__(self):
        self.pn = []

        super().__init__()

    def visit_BinOp(self, node):
        self.visit(node.op)
        self.visit(node.left)
        self.visit(node.right)

    def visit_Add(self, node):
        self.pn.append(dict(label='+', type='binop'))

    def visit_Sub(self, node):
        self.pn.append(dict(label='-', type='binop'))

    def visit_Mult(self, node):
        self.pn.append(dict(label='*', type='binop'))

    def visit_Div(self, node):
        self.pn.append(dict(label='/', type='binop'))

    def visit_Pow(self, node):
        self.pn.append(dict(label='^', type='binop'))

    def visit_Num(self, node):
        self.pn.append(dict(label=node.n, type='num'))


@app.route('/display', methods=['POST'])
async def display(request):
    """Return a json to display in client.

    Request must include `expr`.
    """
    tree = ast.parse(request.json['expr'])
    visitor = PolishNotationVisitor()
    visitor.visit(tree)

    return json(visitor.pn)
