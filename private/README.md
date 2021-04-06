# Private directory

Keep this directory private! Most secure if it is created on your server and never leaves the server.

## acme-dns-provider.key

Traefik needs your `acme-dns-provider.key` file to contain a valid API token from your DNS provider. See [https://doc.traefik.io/traefik/https/acme/#providers](https://doc.traefik.io/traefik/https/acme/#providers)

## acme.json

Traefik will store all of your Letsencrypt-issued SSL certificates and their private keys inside of the `acme.json` file in this directory.

You just need a blank file to start. Make sure to restrict file permissions.

```bash
$ touch acme.json
$ chmod 600 acme.json
```

See [https://doc.traefik.io/traefik/https/acme/](https://doc.traefik.io/traefik/https/acme/)
