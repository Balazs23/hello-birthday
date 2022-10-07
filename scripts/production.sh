#!/bin/bash
set -e

RED='\033[0;31m'
NC='\033[0m' # No Color
echo -e "${RED}Migrate traffic from latest (preview) version of application${NC}"

source .project.env

gcloud run services update-traffic $GCP_SERVICE_NAME \
--region $GCP_REGION \
--clear-tags \
--to-latest