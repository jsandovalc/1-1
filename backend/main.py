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
        self.root = {}

        super().__init__()

    def visit_BinOp(self, node):
        if not self.root:
            node.op.work_on = self.root
            self.visit(node.op)
            self.root['left'] = {}
            node.left.work_on = self.root['left']
            self.visit(node.left)
            self.root['right'] = {}
            node.right.work_on = self.root['right']
            print(3)
            self.visit(node.right)
        else:
            node.op.work_on = node.work_on
            self.visit(node.op)
            node.work_on['left'] = {}
            node.left.work_on = node.work_on['left']
            self.visit(node.left)
            node.work_on['right'] = {}
            node.right.work_on = node.work_on['right']
            self.visit(node.right)

    def visit_Add(self, node):
        node.work_on['label'] = '+'
        node.work_on['type'] = 'binop'

    def visit_Sub(self, node):
        node.work_on['label'] = '-'
        node.work_on['type'] = 'binop'

    def visit_Mult(self, node):
        node.work_on['label'] = '*'
        node.work_on['type'] = 'binop'

    def visit_Div(self, node):
        node.work_on['label'] = '/'
        node.work_on['type'] = 'binop'

    def visit_Pow(self, node):
        node.work_on['label'] = '^'
        node.work_on['type'] = 'binop'

    def visit_Num(self, node):
        node.work_on['type'] = 'num'
        node.work_on['label'] = node.n


@app.route('/display', methods=['POST'])
async def display(request):
    """Return a json to display in client.

    Request must include `expr`.
    """
    tree = ast.parse(request.json['expr'])
    visitor = PolishNotationVisitor()
    visitor.visit(tree)

    return json(visitor.root)
