#!/bin/bash

set -exu

ARCH=$1
IMAGE=$(perl -ne 'print $1 if /FROM\s+(.*)/' "Dockerfile")
ROOT=$(cd "$(dirname "$0")/../" && pwd)

PLATFORM=unknown
if [[ "$ARCH" = "x86_64" ]]; then
    PLATFORM=linux/amd64
fi
if [[ "$ARCH" = "aarch64" ]]; then
    PLATFORM=linux/arm64
fi

docker run \
    --rm \
    -v "$ROOT/$ARCH.build:/build" \
    --platform "$PLATFORM" \
    "$IMAGE" \
    sh -c "yum update -y && yum install -y \"/build/RPMS/\$(uname -m)\"/*.rpm && mssqldef --help && mysqldef --help && psqldef --help && sqlite3def --help"
