# SSL certificate directory

Traefik looks for `acme.json` in this directory. Traefik will store all of your Letsencrypt-issued SSL certificates and their private keys inside of `acme.json`.

You just need a blank file to start. Make sure to restrict file permissions.

```bash
$ touch acme.json
$ chmod 600 acme.json
```

See [https://doc.traefik.io/traefik/https/acme/](https://doc.traefik.io/traefik/https/acme/)

