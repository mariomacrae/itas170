Week 9 starter

  site/               index, a custom 404, a docs/ folder
  nginx/default.conf  the server block for Part 1 (Part 2 adds the /api/ proxy)
  Dockerfile          nginx + conf + site, baked in — the deployable image
  compose.yml         web (built) + whoami
  .env.example        the shape of a secrets file; copy to .env (ignored), never commit .env
  ports.md            your port on the department Docker host, once it is
                      ready (not used today: Part 3 uses a pretend host)
  tailnet/            Part 4b: the same site behind a Tailscale sidecar on YOUR tailnet
    compose.yml         tailnet (tailscale/tailscale) + web (nginx, sharing its network)
    serve.json          HTTPS on 443 → port 80 inside; a real certificate for the name
    .env.example        TS_AUTHKEY= — copy to .env, paste your auth key, never commit
