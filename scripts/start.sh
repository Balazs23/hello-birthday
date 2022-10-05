#!/bin/bash
MONGO_URI="mongodb://mongo:27017/" uvicorn --app-dir ./src/ api:app