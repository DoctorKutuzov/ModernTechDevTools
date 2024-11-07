import uvicorn as uvicorn
from fastapi import FastAPI

from app.routers import users_router

app = FastAPI(
    title='ModernTechDevTools'
)

app.include_router(users_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80)
