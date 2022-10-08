#!/bin/bash
set -e

pushd scripts
source common.sh
popd

source .project.env
echo -e "${GREEN}Please authenticate into $GCP_PROJECT_ID!, gcloud sdk required${NC}"
gcloud auth login
gcloud config set project $GCP_PROJECT_ID
gcloud config set run/region $GCP_REGION
gcloud auth application-default login