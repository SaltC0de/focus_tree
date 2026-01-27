from fastapi import FastAPI
from routers.auth import router as auth_router
from routers.users import router as users_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

app.include_router(auth_router)
app.include_router(users_router)