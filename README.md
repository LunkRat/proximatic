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

The entire app could be built using only Traefik container configuration files like this one:

https://gist.github.com/containeroo-gists/b896f685cd8fd2f4f6ac3d823f044436

The Admin UI could simply read and write Traefik configuration YML for the Traefik container.

Docker or K8s deployed via Ansible.

That's it!
