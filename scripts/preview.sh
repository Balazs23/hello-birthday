#!/bin/bash
set -e

RED='\033[0;31m'
NC='\033[0m' # No Color
echo -e "${YELLOW}Deploying application for preview${NC}"

source .project.env

gcloud run deploy $GCP_SERVICE_NAME \
--source . \
--region $GCP_REGION \
--service-account=$GCP_SERVICE_ACCOUNT_ID@$GCP_PROJECT_ID.iam.gserviceaccount.com \
--set-cloudsql-instances=$GCP_PROJECT_ID:$GCP_REGION:$GCP_DATABASE_INSTANCE \
--set-env-vars INSTANCE_CONNECTION_NAME=$GCP_PROJECT_ID:$GCP_REGION:$GCP_DATABASE_INSTANCE,DB_IAM_USER=$GCP_SERVICE_ACCOUNT_ID@$GCP_PROJECT_ID.iam,DB_NAME=$GCP_DATABASE_NAME \
--allow-unauthenticated \
--no-traffic \
--tag=preview