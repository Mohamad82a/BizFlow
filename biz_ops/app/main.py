from fastapi import FastAPI, status
from .routers import routes

app = FastAPI()
app.include_router(routes.router)
@app.get('/')
def sayhello():
    return 'Welcome to BizOps Service!'


