# Default target
.PHONY: build_api build-local-dev

# Load environment variables from .env file
include .env
export

all: build_api

build_api:
	#!/bin/bash



	# Build the Docker image
	echo "Building Docker image: ${IMAGE_NAME}:${DOCKER_TAG}"
	docker build -t "${IMAGE_NAME}:${DOCKER_TAG}" .

	# Remove any existing container with the same name
	echo "Stopping and removing existing container (if any)..."
	docker rm -f "${CONTAINER_NAME}" || true

	# Run the Docker container
	echo "Running Docker container: ${CONTAINER_NAME}"
	docker run --env-file .env --name "${CONTAINER_NAME}" --network host "${IMAGE_NAME}:${DOCKER_TAG}"

	# Output container status
	docker ps -a | grep "${CONTAINER_NAME}"

build-local-dev:
	@echo "Building local development environment..."
	cd .local_dev && $(MAKE)
