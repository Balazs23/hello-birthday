#!/bin/bash
set -e

pushd scripts
source common.sh
popd

echo -e "${GREEN}installing required lib(s) for applicatio test${NC}"
pip install -r test-requirements.txt
echo -e "${GREEN}starting test(s)${NC}"
coverage run -m pytest && coverage report -m --skip-empty