#!/bin/bash
set -e

pushd scripts
source common.sh
popd

echo -e "${YELLOW}removing local image${NC}"
docker rmi $LOCAL_IMAGE