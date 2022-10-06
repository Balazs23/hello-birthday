#!/bin/bash
set -e

RED='\033[0;31m'
NC='\033[0m' # No Color
echo -e "${RED}GCP login is required!${NC}, run init-gcloud.sh once before deploying infra"

pushd terragrunt/prod
terragrunt run-all plan
terragrunt run-all apply