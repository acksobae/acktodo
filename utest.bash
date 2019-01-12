#!/usr/bin/env bash

count=1
while true; do
    clear
    clear
    echo "Count: $count"
    count=$((count+1))
    ./setup.py test 2>&1
    if [[ "$?" != 0 ]]; then
        git add -A
        git commit -m "(auto commit)"
    fi
    inotifywait  -r */* -qq -e create -e delete -e modify
done