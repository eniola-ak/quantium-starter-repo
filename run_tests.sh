#!/usr/bin/env bash

set -e

cd "$(dirname "$0")"
if [ ! -d ".venv" ]; then
  echo "Virtual environment .venv not found."
  exit 1
fi

source .venv/bin/activate

pytest
status=$?

deactivate || true

if [ $status -eq 0 ]; then
  exit 0
else
  exit 1
fi
