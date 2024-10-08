from fastapi import FastAPI


api: FastAPI = FastAPI(
    title="Smart Menu AI",
)

@api.get("/")
def hello():
    return {"greeting": "Hello, world!"}
