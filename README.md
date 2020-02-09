## Some to-do
- Dockerized frontend apps [DONE]
- Add frontend manifest k8s [DONE]
- Testing local deployment frontend + backend top of k8s [DONE tested on KIND]
------------------------
- Create istio manifest [DONE]
- test it on local again [DONE]
------------------------
- Deploy apps and istio on gcp [DONE]
- Check n testing apps [DONE works!]
- Visualize on kiali [WORK AS FCK]

## What's next?
- More deep dive on testing mTLS (wireshark done, ssldump done)
- Deep dive on testssl.sh (try to find on client + server side) --> Still work on Istio-pilot as open PKI :)


## Some snippet debuging

echo "`curl --write-out '%{time_total}' --silent --output /dev/null http://example.com`" | tee -a some.txt
awk '{ total += $1; count++ } END { print total/count }' some.txt




