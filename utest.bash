#!/usr/bin/env bash

count=1
while true; do
    clear
    clear
    echo "Count: $count"
    count=$((count+1))
    ./setup.py test
    inotifywait  -r */* -qq -e create -e delete -e modify
done