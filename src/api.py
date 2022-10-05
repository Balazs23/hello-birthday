import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from endpoints.hello import router as hello_router
from models.user import Base
from settings import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}


app.include_router(hello_router, tags=["hello"])

if __name__ == "__main__":
    uvicorn.run(app)
