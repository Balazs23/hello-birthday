#!/bin/bash
set -e

source .project.env
gcloud auth login
gcloud config set project $GCP_PROJECT_ID
gcloud auth application-default login