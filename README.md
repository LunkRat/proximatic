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
2. Copy the example files to real files:

```bash
cp docker-compose.example.yml docker-compose.yml
cp conf/traefik.example.yml conf/traefik.yml
cp conf/config.example.yml conf/config.yml
```

3. Edit `docker-compose.yml`, replace all instances of `yourdomain.org` with your domain name, and set the username/password for the Traefik Dashboard basic auth
4. Edit `conf/config.yml` and replace all instances of `yourdomain.org` with your domain name
5. Edit `conf/traefik.yml` and replace `youremail@yourdomain.org` with your email (for LetsEncrypt certificate auto-renewal)
6. Create the docker network used by Proximatic:

```bash
docker network create proxy
```

7. Bring up your Proximatic container with `docker-compose up -d`

## Usage

The configuration file examples have a default domain set up to proxy the Hacker News website [https://news.ycombinator.com/](https://news.ycombinator.com/) through `hackernews.yourdomain.org`. 

To use Hacker News through your Proximatic proxy, visit [https://hackernews.yourdomain.org](https://hackernews.yourdomain.org) in your browser.

Your Proximatic instance provides a Traefik dashboard at `https:traefik.yourdomain.org` with the credentials you set in `docker-compose.yml`.

## License

The MIT License (MIT)
