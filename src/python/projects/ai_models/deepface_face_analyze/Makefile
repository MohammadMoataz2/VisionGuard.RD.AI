# Define variables
include .env
export

# Declare phony targets to prevent conflicts with filenames
.PHONY: install-dependencies train-model check-env-vars build-docker-image stop-remove-container run-docker-container all

# Main target to run everything
all: run-docker-container

# Install dependencies
install-dependencies:
	@echo "Installing dependencies from requirements.txt..."
	pip install -r requirements.txt

# Train the model
train-model:
	@echo "Training the model..."
	python face_analyze/train.py

# Check if required environment variables are set
check-env-vars:
	@echo "Checking environment variables..."
	@if [ -z "$(DOCKER_IMAGE_TAG)" ] || [ -z "$(DOCKER_IMAGE_VERSION)" ]; then \
		echo "DOCKER_IMAGE_TAG or DOCKER_IMAGE_VERSION is not set in the .env file."; \
		exit 1; \
	fi
	@echo "Environment variables are set correctly."

# Build the Docker image
build-docker-image: install-dependencies train-model check-env-vars
	@echo "Building Docker image with tag: $(DOCKER_IMAGE_TAG):$(DOCKER_IMAGE_VERSION)..."
	$(eval FULL_TAG=$(DOCKER_IMAGE_TAG):$(DOCKER_IMAGE_VERSION))
	docker build -t $(FULL_TAG) .

# Stop and remove existing container if it exists
# Stop and remove existing container if it exists
stop-remove-container:
	@echo "Checking if the container already exists..."
	@if [ "$(shell docker ps -a -q -f name=$(DOCKER_IMAGE_TAG))" ]; then \
		echo "Container '$(DOCKER_IMAGE_TAG)' exists. Stopping and removing it..."; \
		docker stop $(DOCKER_IMAGE_TAG); \
		docker rm $(DOCKER_IMAGE_TAG); \
	else \
		echo "No existing container found with the name '$(DOCKER_IMAGE_TAG)'."; \
	fi


# Run the Docker container
run-docker-container: build-docker-image stop-remove-container
	@echo "Running Docker container from image: $(FULL_TAG)..."
	docker run --network host --env-file .env --name $(DOCKER_IMAGE_TAG) $(FULL_TAG)


