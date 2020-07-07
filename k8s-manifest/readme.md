## Section k8s-manifest

Just apply with: 

```
kubectl apply -f apps-dep.yaml
```

Ps:

if you run with kubernetes cluster version `>= v.1.16` will get error about deployment [API Deprecated](https://kubernetes.io/blog/2019/07/18/api-deprecations-in-1-16/), fix it with:

```
kubectl convert -f k8s-manifest/apps-dep.yaml | k apply -f -
```