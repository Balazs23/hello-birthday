#!/bin/bash
set -e

pushd scripts
source common.sh
popd

echo -e "${GREEN}installing required lib(s) for application${NC}"
pip install --user -r requirements.txt