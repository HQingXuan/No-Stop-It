#!/bin/sh
set -e
asciidoctor -o docs/usage.html docs/usage.adoc
echo "docs/usage.html regenerated"
