all: run


build:
	docker build . -t dmsa-simple-app:0.0.1

run:
	docker run --rm -p 5000:5000 dmsa-simple-app:0.0.1

push:
	docker tag dmsa-simple-app:0.0.1 \
		europe-west1-docker.pkg.dev/learning-281911/dmsa-test/dmsa-simple-app:0.0.1
	docker push europe-west1-docker.pkg.dev/learning-281911/dmsa-test/dmsa-simple-app:0.0.1
