```bash
▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖    ▗▄▄▖ ▗▄▄▄▖ ▗▄▄▖ ▗▄▖ ▗▖  ▗▖    ▗▄▄▖ ▗▖    ▗▄▖▗▄▄▄▖▗▄▄▄▖ ▗▄▖ ▗▄▄▖ ▗▖  ▗▖
  █  ▐▌ ▐▌▐▌       ▐▌ ▐▌  █  ▐▌   ▐▌ ▐▌▐▛▚▖▐▌    ▐▌ ▐▌▐▌   ▐▌ ▐▌ █  ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌
  █  ▐▛▀▜▌▐▛▀▀▘    ▐▛▀▚▖  █   ▝▀▚▖▐▌ ▐▌▐▌ ▝▜▌    ▐▛▀▘ ▐▌   ▐▛▀▜▌ █  ▐▛▀▀▘▐▌ ▐▌▐▛▀▚▖▐▌  ▐▌
  █  ▐▌ ▐▌▐▙▄▄▖    ▐▙▄▞▘▗▄█▄▖▗▄▄▞▘▝▚▄▞▘▐▌  ▐▌    ▐▌   ▐▙▄▄▖▐▌ ▐▌ █  ▐▌   ▝▚▄▞▘▐▌ ▐▌▐▌  ▐▌                                                                                 
```

## Table of Contents
* [Overview](#overview)
* [Shiny Proxy](#shiny-proxy)
  * [Local Development](#local-development)
  
## Overview
I am going to immediately regret this monolithic application.

## Shiny Proxy
### Local Development
#### via Docker
1. To build the image.
```bash
docker build --build-arg TBP_COGNITO_CLIENT_ID --build-arg TBP_COGNITO_CLIENT_SECRET --build-arg TBP_COGNITO_PREFIX_DOMAIN --build-arg TBP_COGNITO_USER_POOL_ID -t tbp/tbp-shiny-proxy .
```
2. To run the image.
```bash
docker run --env-file ../.env -p 8080:8080 tbp/tbp-shiny-proxy
```