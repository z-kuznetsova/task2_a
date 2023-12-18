from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def f_index():
    return ('Кузнецова Злата')


@app.get("/tools")
async def f_indexT():
    return ('Любитель')


@app.get("/users")
async def f_indexT():
    return ('892939856')
