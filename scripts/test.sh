#!/bin/bash
pip install -r test-requirements.txt
coverage run -m pytest && coverage report -m