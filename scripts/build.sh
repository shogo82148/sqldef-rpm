#!/bin/bash

set -exu

ROOT=$(cd "$(dirname "$0")/../" && pwd)
PLATFORM=$1

VERSION=0.13.16
IMAGE_NAME=sqldef-package-$PLATFORM
TARGZ_FILE=sqldef.tar.gz

rm -rf "$PLATFORM.build.bak"
if [[ -d "$PLATFORM.build" ]];
then
    mv "$PLATFORM.build" "$PLATFORM.build.bak"
fi

GOARCH=unknown
if [[ "$PLATFORM" = "x86_64" ]]; then
    GOARCH=amd64
fi
if [[ "$PLATFORM" = "aarch64" ]]; then
    GOARCH=arm64
fi

docker build \
    --build-arg VERSION="$VERSION" \
    --build-arg GOARCH="$GOARCH" \
    --build-arg PLATFORM="$PLATFORM" \
    -t "$IMAGE_NAME" "$ROOT"

docker run --name "$IMAGE_NAME-tmp" "$IMAGE_NAME"
mkdir -p "$ROOT/tmp"
docker wait "$IMAGE_NAME-tmp"
docker cp "$IMAGE_NAME-tmp:/tmp/$TARGZ_FILE" "$ROOT/tmp"
docker rm "$IMAGE_NAME-tmp"

mkdir -p "$PLATFORM.build"
tar -xzf "$ROOT/tmp/$TARGZ_FILE" -C "$PLATFORM.build"
rm -rf "$ROOT/tmp"
