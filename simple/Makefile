make: run

run:
	kubectl apply -f .

stop:
	kubectl delete services/dmsa-simple-app-ui
	kubectl delete deployments/dmsa-simple-app

create-argo-app:
	argocd app create dmsa-simple-app --repo https://github.com/samarkanov/dmsa-k8s-apps.git \
		--path simple \
		--dest-server https://kubernetes.default.svc \
		--dest-namespace default

sync-argo:
	argocd app sync dmsa-simple-app

port-forward:
	kubectl port-forward svc/dmsa-simple-app-ui 5000:5000 --address 0.0.0.0
