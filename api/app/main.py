import os
import glob
import yaml
import requests
from fastapi import FastAPI, status
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader

class DomainUpdate(BaseModel):
    """Pydantic model for updating a domain."""
    subdomain: str # The subdomain on which to proxy the URL
    url: str       # The URL to proxy

class DomainDelete(BaseModel):
    """Pydantic model for deleting a domain."""
    subdomain: str


app = FastAPI()


@app.get("/")
def read_root():
    """Endpoint returning basic information."""

    return {'Proximatic':'API'}

@app.get("/domains/list")
def get_domains():
    """Endpoint that returns a list of configured domains."""

    response = {
      'domains': []
    }
    files = glob.glob("/data/traefik/conf/*.yml")
    for filename in files:
        with open(filename, 'r') as yml_stream:
            config = yaml.safe_load(yml_stream)
            for service, values in config['http']['services'].items():
                response['domains'].append({service:values['loadBalancer']['servers'][0]['url']})
    return response

@app.post("/domains/update", status_code=status.HTTP_201_CREATED)
async def domain_update(item: DomainUpdate):
    """Endpoint that creates or replaces a domain configuration .yml file."""

    # Check the URL for validity by visiting it expecting a 200 response code from its server.
    try:
        result = requests.get(item.url).status_code
        if result != 200:
            status_code = 400
            return {"Error":"Invalid URL"} # @todo define some reusable error response payloads.
    except Exception as e:
        status_code = 400
        return {"error":"Invalid URL", "msg":str(e)}

    # Load Jinja2 template engine.
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template('domain.j2.yml')
    # Use template to generate a string of YAML containing valid Traefik config.
    yml_string = template.render(
                   subdomain=item.subdomain,
                   proximatic_fqdn=os.getenv('PROXIMATIC_FQDN'),
                   url=item.url
                 )
    # Write the YAML to a .yml file named after the subdomain.
    yml_file = open(r"/data/traefik/conf/" + item.subdomain + ".yml", 'wt')
    lines_written = yml_file.write(yml_string)
    yml_file.close()

    return item

@app.post("/domains/delete")
async def domain_delete(item: DomainDelete):
    if os.path.exists("/data/traefik/conf/" + item.subdomain + ".yml"):
        os.remove("/data/traefik/conf/" + item.subdomain + ".yml")
    return item
