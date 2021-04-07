# Proximatic

Serve any website URL from your own domain.

## Requirements

- Docker engine running on any publicly accessible server
- `docker-compose` installed on the server
- A domain with nameservers pointed to a supported ACME DNS provider
- A wildcard DNS `A` record for `*.PROXIMATIC_FQDN` pointed to your server's public IPv4 and IPv6 addresses
- A read/write API token from your ACME-supported DNS provider

## Installation

1. Clone this repository into `/opt` on your server and change your directory to `/opt/proximatic`
2. Copy the `example.env` to `.env` and replace the values for `PROXIMATIC_FQDN`, `ACME_EMAIL`, and `ACME_DNS_PROVIDER`
3. Run `touch /opt/proximatic/private/acme.json && chmod 600 /opt/proximatic/private/acme.json`
4. Create the file `/opt/proximatic/private/acme-dns-provider.key` containing only your DNS-provider API token.
3. Create the external network needed for `docker-compose`
```bash
docker network create proxy
```
4. Bring up your Proximatic container with `docker-compose up -d --build`

## Usage

Proximatic uses the concept of a 'provider' to define a subdomain of your `PROXIMATIC_FQDN` that
serves/proxies an external server URL. You create Proximatic providers by passing a provider `id` and `server` strings to the `proximatic-create` command/function/endpoint. You can manage providers using the `proximatic` CLI, or using the REST API, or using the Python API.

### CLI usage

You can use the `proximatic` command inside your `proximatic_api` container to add a new provider, list your created providers, and delete providers.

Create a provider by command line from your Proximatic server:

#### Run it

```bash
docker exec -it proximatic_api proximatic provider-create example https://www.example.org
```

#### Check it

Now type `docker exec -it proximatic_api proximatic provider-list` and you should see:

```markdown
| type     | id      | endpoint                  | server                  |
|----------|---------|---------------------------|-------------------------|
| provider | example | example.`PROXIMATIC_FQDN` | https://www.example.org |
```

The website at `https://www.example.org` is now served by proxy at your subdomain `https://example.PROXIMATIC_FQDN`

### Rest API usage

You can manage providers via REST calls to your Proximatic REST API endpoint: `https://api.PROXIMATIC_FQDN/`

HTML API endpoints (interactive docs):

- `https://api.PROXIMATIC_FQDN/docs`
- `https://api.PROXIMATIC_FQDN/redoc`

### Python API

Proximatic core is a [Python package](https://pypi.org/project/proximatic/) that you can `import` into your scripts. For usage, see [https://github.com/LunkRat/proximatic-api](https://github.com/LunkRat/proximatic-api)

## License

The MIT License (MIT)
