#!/bin/sh
# Frees disk by clearing local data.
rm -rf "$(dirname "$0")/../data"/*
