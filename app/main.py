from fastapi import FastAPI
from routers import task, user

app = FastAPI()


@app.get('/')
async def start():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)


# Запуск сервера осуществите командами
# cd app (эта команда позволяет попасть в папку app - в этой папке находится файл main)
# затем
# python -m uvicorn main:app