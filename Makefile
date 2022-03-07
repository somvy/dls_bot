all: run

run: build-docker
	$(info Make: run docker)
	docker run -t dls_bot

build-docker:
	$(info Make: build docker)
	docker build -t dls_bot .
