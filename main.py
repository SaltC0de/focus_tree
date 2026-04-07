from fastapi import FastAPI

from routers.auth import router as auth_router
from routers.focus_settings import router as focus_settings_router
from routers.users import router as users_router


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(focus_settings_router)