import uvicorn
from fastapi import FastAPI  # FastAPIを使うために必要
from pydantic import BaseModel  # リクエストbodyを定義するために必要

app = FastAPI()


class post_string(BaseModel):
    param: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/post")
def return_post_string(p: post_string):
    return p.param


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
