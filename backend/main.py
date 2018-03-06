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
    print(request.json)
    return json({'result': eval(request.json['expr'],
                                request.json['table'])})
