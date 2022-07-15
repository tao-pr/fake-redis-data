# Elasticache Fake Data

Generate fake data inside Elasticache redis instance (non-cluster mode)


## Prerequisites

First off, tunnel to the target Elasticache redis endpoint in a separate process

```sh
zkubectl tunnel <WHATEVER_ENDPOINT_URL>.cache.amazonaws.com 6378:6379
```

Optional, ensure you have an access with your CLI

```sh
redis-cli -p 6378
> hmget <MAPKEY> <KEY> # blah blah
```

## How to run

TBD

