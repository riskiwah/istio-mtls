#!/bin/bash
for ((i=0;i<=4;i++));do
    echo "`curl --write-out '%{time_total}' --silent --output /dev/null http://localhost`" | tee -a some.txt
    sleep 2
done
awk '{ total += $1; count++ } END { print total/count }' some.txt
