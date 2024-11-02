Create k8s secrets

kubectl create secret generic gcp-artifact-registry \
    --from-file=.dockerconfigjson=$HOME/.docker/config.json \
    --type=kubernetes.io/dockerconfigjson
