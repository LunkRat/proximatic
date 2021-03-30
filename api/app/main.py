from fastapi import FastAPI
import yaml
import json
app = FastAPI()


@app.get("/")
def read_root():
    with open(r'config.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
        config = yaml.load(file, Loader=yaml.FullLoader)
    return {json.dumps(config)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
