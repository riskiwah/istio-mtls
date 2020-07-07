#!/bin/bash

for ((i=1;i<=10;i++));
do
    curl http://localhost/ > /dev/null 2>&1
    echo "hehehe ke $i"
    sleep 2
done 