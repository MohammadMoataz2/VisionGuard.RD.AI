#!/bin/bash

# Load environment variables from .env file
set -o allexport
source .env
set +o allexport

# Check if all necessary environment variables are set
if [ -z "$API_DOCKER_IMAGE_NAME" ] || [ -z "$API_DOCKER_CONTAINER_NAME" ] || [ -z "$API_DOCKER_TAG" ]; then
  echo "Error: One or more Docker environment variables are not set in the .env file."
  exit 1
fi

# Build the Docker image
echo "Building Docker image: $API_DOCKER_IMAGE_NAME:$API_DOCKER_TAG"
docker build -t "$API_DOCKER_IMAGE_NAME:$API_DOCKER_TAG" .

# Remove any existing container with the same name
echo "Stopping and removing existing container (if any)..."
docker rm -f "$API_DOCKER_CONTAINER_NAME" || true



echo "Opening the browser with the web app URL: $API_CONN_STR"

# Open the browser (works on Linux and macOS; modify for Windows if needed)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open $API_CONN_STR
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open $API_CONN_STR
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" ]]; then
    start $API_CONN_STR
else
    echo "Unsupported OS, please open the browser manually."
fi

# Run the Docker container
echo "Running Docker container: $API_DOCKER_CONTAINER_NAME"
docker run --env-file .env --name "$API_DOCKER_CONTAINER_NAME" --network host  "$API_DOCKER_IMAGE_NAME:$API_DOCKER_TAG"

# Output container status
docker ps -a | grep "$API_DOCKER_CONTAINER_NAME"



