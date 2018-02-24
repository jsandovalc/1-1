from sanic import Sanic
from sanic.response import json, file

app = Sanic()

app.static('/static', './dist/static')

@app.route('/')
async def index(request):
    return await file('dist/index.html')
