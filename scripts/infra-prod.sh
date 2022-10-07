#!/bin/bash
set -e

pushd scripts
source common.sh
popd

echo -e "${RED}GCP login is required!${NC}, run init-gcloud.sh once before deploying infra"

source .project.env

echo -e "${RED}(!) Production infrastucture deployment"
pushd terragrunt/prod
terragrunt run-all plan
terragrunt run-all apply