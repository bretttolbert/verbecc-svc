#!/bin/bash
docker-compose -f docker-compose.common.yml -f docker-compose.dev.yml run --rm --entrypoint pytest python $*
