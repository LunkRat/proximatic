# Proximatic

Serve any website URL from your own domain.

## Aims

- Modern http/2 web proxy
- Simple configuration
- Admin UI for configuring domains to proxy, include/exclude rules
- Web UI that allows you to input a URL and it will give you back a proxied URL that serves the original URL through your domain/server
- Ability to require authentication when users visit proxied URLs
- Support major authentication providers and identity providers: Oauth, Shibboleth, http auth, IP whitelist.
- Automated SSL certificates
- Scalability
- High-availability

## Plan

The entire proxy engine could be built using only Traefik container configuration files.

The Admin UI could simply read and write Traefik configuration YML for the Traefik container.

Docker or K8s deployed via Ansible.

That's it!

## Proof of concept

It works. You can follow the instructions below to bring up Proximatic on any Docker engine.

## Requirements

- Docker engine running on a publicly accessible server
- docker-compose
- A domain with a wildcard DNS for `*.yourdomain.org` or individual `AAA` records for each domain that you want to proxy.

## Installation

1. Clone this repository into `/opt` and change your directory to `/opt/proximatic`
2. Copy the `example.env` to `.env` and replace examples with real values.
3. Create the external network needed for `docker-compose`
```bash
docker network create proxy
```
4. Bring up your Proximatic container with `docker-compose up -d`

## Usage

### Using Proxied URLs

The configuration file examples have a default domain set up to proxy the Hacker News website [https://news.ycombinator.com/](https://news.ycombinator.com/) through `hackernews.yourdomain.org`. 

To use Hacker News through your Proximatic proxy, visit [https://hackernews.yourdomain.org](https://hackernews.yourdomain.org) in your browser.

Your Proximatic instance provides a Traefik dashboard at `https:traefik.yourdomain.org` with the credentials you set in `docker-compose.yml`.

### Rest API

Json endpoint: [https://api.yourdomain.org](https://api.yourdomain.org)

HTML API endpoints (interactive docs): 

- [https://api.yourdomain.org/docs](https://api.yourdomain.org/docs)
- [https://api.yourdomain.org/redoc](https://api.yourdomain.org/redoc)

## License

The MIT License (MIT)
