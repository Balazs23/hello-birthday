#!/bin/bash
set -e

pushd scripts
source common.sh
popd


if [[ "$(docker images -q $LOCAL_IMAGE 2> /dev/null)" == "" ]]; then
  echo -e "${RED}missing local image, building one${NC}"
  bash scripts/build.sh
fi

# postgresql://foo:bar@somewhere:5432/mydatabase
DATABASE_URL=${1:-"none"}

if [ $DATABASE_URL == "none" ]; then
    echo -e "${GREEN}starting container for preview with non persistent sqlite mode${NC}"
    docker run --rm --publish 8080:8080 $LOCAL_IMAGE
else
    echo -e "${GREEN}starting container with $DATABASE_URL db string${NC}"
    docker run --rm --publish 8080:8080 --env DATABASE_URL=$DATABASE_URL $LOCAL_IMAGE
fi