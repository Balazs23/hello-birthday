#!/bin/bash
set -e

pushd scripts
source common.sh
popd
source .project.env

usage()
{
  echo "Usage: preview [OPTION]
                At most one of these can be specified:
                [ -d | --deploy ] : deploy current codebase as revision GREEN
                [ -t 1..100 | --traffic  100] : split traffic to rev GREEN with the given precentage
                [ -r | --rollback  ] : rollback 100% traffic to revision BLUE
                [ -p | --production  ] : make revision GREEN as current production version - BLUE
                [ -h | --help  ]" 
}

deploy()
{
    echo -e "${YELLOW}Deploying application for preview${NC} and tagging revision as ${GREEN}GREEN${NC}"

    gcloud run deploy $GCP_SERVICE_NAME \
    --source . \
    --region $GCP_REGION \
    --service-account=$GCP_SERVICE_ACCOUNT_ID@$GCP_PROJECT_ID.iam.gserviceaccount.com \
    --set-cloudsql-instances=$GCP_PROJECT_ID:$GCP_REGION:$GCP_DATABASE_INSTANCE \
    --set-env-vars INSTANCE_CONNECTION_NAME=$GCP_PROJECT_ID:$GCP_REGION:$GCP_DATABASE_INSTANCE,DB_IAM_USER=$GCP_SERVICE_ACCOUNT_ID@$GCP_PROJECT_ID.iam,DB_NAME=$GCP_DATABASE_NAME \
    --allow-unauthenticated \
    --no-traffic \
    --tag=green

    echo -e "${GREEN}You can check logs running preview-logs.sh script${NC}"

    exit 0
}

rollback(){
    echo -e "${RED}Rolling back to revision BLUE${NC}"
    gcloud run services update-traffic $GCP_SERVICE_NAME \
    --region=$GCP_REGION \
    --to-tags blue=100
    exit 0
}

traffic()
{
    declare -i p=$1
    if [ "$p" -eq "0" ]; 
    then
        echo "use rollback option!"
        exit 0
    fi
    echo -e "${YELLOW}Splitting $p % of traffig to revision ${NC}${GREEN}GREEN${NC}"
    gcloud run services update-traffic $GCP_SERVICE_NAME \
    --region=$GCP_REGION \
    --to-tags green=$p
    exit 0
}

production()
{
    echo -e "${YELLOW}Migrate GREEN revision to BLUE with 100% traffic${NC}"
    gcloud run services update-traffic $GCP_SERVICE_NAME \
    --region $GCP_REGION \
    --set-tags=blue=LATEST \
    --to-latest
    exit 0
}


SHORT=d,p,r,t:,h
LONG=deploy,rollback,production,traffic:,help
OPTS=$(getopt -a -n preview --options $SHORT --longoptions $LONG -- "$@")

eval set -- "$OPTS"

while :
do
  case "$1" in
    -d | --deploy )
        deploy
        ;;
    -p | --production )
        production
        ;;    
    -r | --rollback )
        rollback
        ;;
    -t | --traffic )
        traffic $2
        ;;
    -h | --help)
      usage
      exit 2
      ;;
    --)
      shift;
      break
      ;;
    *)
      echo "Unexpected option: $1"
      exit 1
      ;;
  esac
done





