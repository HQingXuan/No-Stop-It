#!/bin/sh
# Clears local data. Production users.json is not backed up anywhere else.
rm -rf "$(dirname "$0")/../data"/*
