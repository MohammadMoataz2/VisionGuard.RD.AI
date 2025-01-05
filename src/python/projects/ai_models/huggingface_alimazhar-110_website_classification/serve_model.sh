#!/bin/bash

# Load environment variables from the .env file
if [ -f .env ]; then
  export $(cat .env | xargs)
else
  echo ".env file not found. Please create one with the required variables."
  exit 1
fi

# Check if required environment variables are set
if [[ -z "$DOCKER_IMAGE_TAG" ]] || [[ -z "$DOCKER_IMAGE_VERSION" ]]; then
  echo "DOCKER_IMAGE_TAG or DOCKER_IMAGE_VERSION is not set in the .env file."
  exit 1
fi

# Combine tag and version
FULL_TAG="${DOCKER_IMAGE_TAG}:${DOCKER_IMAGE_VERSION}"

# Build the Docker image
echo "Building Docker image with tag: $FULL_TAG..."
docker build -t "$FULL_TAG" .

# Check if the build was successful
if [ $? -ne 0 ]; then
  echo "Docker build failed."
  exit 1
fi

# Check if the container already exists
if [ "$(docker ps -a -q -f name="$DOCKER_IMAGE_TAG")" ]; then
  echo "Container '$DOCKER_IMAGE_TAG' exists. Stopping and removing it..."
  docker stop "$DOCKER_IMAGE_TAG"
  docker rm "$DOCKER_IMAGE_TAG"
else
  echo "No existing container found with the name '$DOCKER_IMAGE_TAG'."
fi

# Run the Docker container
echo "Running Docker container from image: $FULL_TAG..."
docker run --network host --env-file .env --name "$DOCKER_IMAGE_TAG" "$FULL_TAG"
