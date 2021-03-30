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

@app.get("/domains/list")
def get_domains():
    yaml_file = 'config.yml'
    with open(yaml_file, "r") as fh:
        config = yaml.load(fh, Loader=yaml.SafeLoader)
    response = {
      'domains':{}
    }
    for service, values in config['http']['services'].items():
        response['domains'][service] = values['loadBalancer']['servers'][0]['url']
    return response


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
