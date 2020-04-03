from fastapi import FastAPI
import os

os.environ["SCRIPT_NAME"] = "/a/b/c/d/e"
print("Prefix: ", os.environ["SCRIPT_NAME"])

app = FastAPI(openapi_prefix='banana', root_path='banana')

@app.get("/hello")
def read_root():
    print("???")
    return {"Hello": "World"}

@app.get("/hernekeitto")
def read_root():
    return {"Hello": "Keitto"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}