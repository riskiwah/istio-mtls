#!/bin/bash
while true
do
    sleep 2
    curl http://localhost  > /dev/null 2>&1
    echo "hehe"
done 