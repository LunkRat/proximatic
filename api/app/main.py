import os
from fastapi import FastAPI, status
from pydantic import BaseModel
from proximatic import Proximatic


class DomainUpdate(BaseModel):
    """Pydantic model for updating a domain."""
    subdomain: str # The subdomain on which to proxy the URL
    url: str       # The URL to proxy

class DomainDelete(BaseModel):
    """Pydantic model for deleting a domain."""
    subdomain: str


app = FastAPI()

proximatic = Proximatic(proximatic_fqdn = os.genenv('PROXIMATIC_FQDN'))

@app.get("/")
def read_root():
    """Endpoint returning basic information."""

    return {'Proximatic':'API'}


@app.get("/domains/list")
def get_domains():
    """Endpoint that returns a list of configured domains."""

    response = proximatic.domains_list()

    return response


@app.post("/domains/update", status_code=status.HTTP_201_CREATED)
async def domain_update(item: DomainUpdate):
    """Endpoint that creates or replaces a domain configuration .yml file."""

    response = proximatic.domain_update(subdomain = item.subdomain, url = item.url)

    return response


@app.post("/domains/delete")
async def domain_delete(item: DomainDelete):
    """Endpoint that deletes a domain configuration .yml file."""

    response = proximatic.domain_delete(item.subdomain)

    return response
