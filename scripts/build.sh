#!/bin/bash
set -e

pushd scripts
source common.sh
popd

echo -e "${GREEN}Using google cloud buildpack${NC}"

if [ ! -f /usr/local/bin/pack ]
then
  echo -e "${YELLOW}Pack lib missing, installing it${NC}"
  architecture="$(uname -m)"
  case ${architecture} in
      x86_64) architecture="amd64";;
      aarch64 | armv8* | arm64) architecture="arm64";;
      aarch32 | armv7* | armvhf*) architecture="arm";;
      i?86) architecture="386";;
      *) echo -e "${RED}(!) Architecture ${architecture} unsupported"; exit 1 ;;
  esac

  unameOut="$(uname -s)"
  case "${unameOut}" in
      Linux*)     machine=linux;;
      Darwin*)    machine=macos;;
      *) echo -e "${RED}(!) Machine ${unameOut} unsupported"; exit 1 ;;
  esac
  echo ${machine}

  (curl -sSL "https://github.com/buildpacks/pack/releases/download/v0.27.0/pack-v0.27.0-${machine}-${architecture}.tgz" | sudo tar -C /usr/local/bin/ --no-same-owner -xzv pack)
fi
pack build $LOCAL_IMAGE \
  --builder gcr.io/buildpacks/builder:v1