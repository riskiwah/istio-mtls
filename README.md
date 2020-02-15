## Some to-do update 10 Feb 2020
- Move Backend API external to owm [work]
- Change Axios frontend api consume variable [work]
- New tag backend and frontend image (owm, owm-k8s) [work]
- Change k8s manifest tag image
- Test it on KinD [DONE AND WORK SMOOTH]

## Some to do on 15 feb 2020
- move service entry to new api external (owm)

## What's next?
- More deep dive on testing mTLS (wireshark done, ssldump done)
- Deep dive on testssl.sh (try to find on client + server side) --> Still work on Istio-pilot as open PKI :)


## Some snippet debuging

echo "`curl --write-out '%{time_total}' --silent --output /dev/null http://example.com`" | tee -a some.txt
awk '{ total += $1; count++ } END { print total/count }' some.txt




