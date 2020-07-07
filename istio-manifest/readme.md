## Section Istio-manifest

For first sailing with:

```
kubectl apply -f istio-manifest/all-in.yaml
```

That's for applying some basic manifest 

If you want dealing with mtls one by one for each services, do:

```
kubectl apply -f istio-manifest/svc-mtls.yaml
```

If you want to enforce all services with mTLS, do:

```
kubectl apply -f istio-manifest/global-mtls.yaml
kubectl apply -f istio-manifest/global-mtls-dr.yaml
```