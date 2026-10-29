#!/bin/sh
set -e
: "${DB_PASSWORD:?DB_PASSWORD is not set}"
python -m unittest -q
