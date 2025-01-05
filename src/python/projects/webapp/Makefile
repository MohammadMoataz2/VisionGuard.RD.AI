

# Default target
.PHONY: all
include .env
export
all: build-image run-container open-browser




# Build the Docker image
.PHONY: build-image
build-image:
	@echo "Building the Docker image..."
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
.PHONY: run-container
run-container:
	@echo "Stopping and removing any existing container..."
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
	@echo "Running the Docker container..."
	docker run --env-file .env --network host -p $(FRONTEND_PORT):$(FRONTEND_PORT) -p $(BACKEND_PORT):$(BACKEND_PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Open the browser
.PHONY: open-browser
open-browser:
	@echo "Opening the browser with the web app URL: $(WEBAPP_CONN_STR)"
	@if [[ "$$OSTYPE" == "linux-gnu"* ]]; then \
	    xdg-open $(WEBAPP_CONN_STR); \
	elif [[ "$$OSTYPE" == "darwin"* ]]; then \
	    open $(WEBAPP_CONN_STR); \
	elif [[ "$$OSTYPE" == "cygwin" || "$$OSTYPE" == "msys" ]]; then \
	    start $(WEBAPP_CONN_STR); \
	else \
	    echo "Unsupported OS, please open the browser manually."; \
	fi
