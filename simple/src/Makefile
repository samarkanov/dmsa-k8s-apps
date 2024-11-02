all: run

TAG := 0.0.8

build:
	docker build . -t dmsa-simple-app:$(TAG)

run:
	docker run --rm -p 5000:5000 dmsa-simple-app:$(TAG)

push:
	docker tag dmsa-simple-app:$(TAG) \
		europe-west1-docker.pkg.dev/learning-281911/dmsa-test/dmsa-simple-app:$(TAG)
	docker push europe-west1-docker.pkg.dev/learning-281911/dmsa-test/dmsa-simple-app:$(TAG)
