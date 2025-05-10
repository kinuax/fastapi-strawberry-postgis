from fastapi import FastAPI

from app.api import graphql_router


app = FastAPI()
app.include_router(graphql_router, prefix="/graphql")


@app.get("/status")
async def status():
    return {"status": "up"}
