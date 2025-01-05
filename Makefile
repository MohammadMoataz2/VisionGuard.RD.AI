# Root Makefile

# Define the paths to the directories containing the .local_dev Makefiles
API_DIR_LOCAL_DEV=src/python/projects/api/.local_dev
API_DIR=src/python/projects/api/
AI_DIR=src/python/projects/ai_models/
WEBAPP_DIR=src/python/projects/webapp/

# Default target
.PHONY: all
all: build-local-dev-api build-local-dev-ai build-ai-models build-api-and-webapp

# Build the local development environment for the API
.PHONY: build-local-dev-api
build-local-dev-api:
	@echo "Building local development environment for API..."
	cd $(API_DIR) && \
	$(MAKE) build-local-dev

# Build the local development environment for AI
.PHONY: build-local-dev-ai
build-local-dev-ai:
	@echo "Building local development environment for AI..."
	cd $(AI_DIR) && \
	$(MAKE) build-local-dev

.PHONY: build-ai-deepface
build-ai-deepface:
	@echo "Building deepface for AI..."
	cd $(AI_DIR) && \
	$(MAKE) build-deepface


.PHONY: build-ai-opencv
build-ai-opencv:
	@echo "Building opencv for AI..."
	cd $(AI_DIR) && \
	$(MAKE) build-opencv


.PHONY: build-ai-website-class
build-ai-website-class:
	@echo "Building website for AI..."
	cd $(AI_DIR) && \
	$(MAKE) build-huggingface-websiteclass

.PHONY: build-ai-models
build-ai-models:
	@echo "Building AI models concurrently..."
	$(MAKE) build-ai-deepface &
	$(MAKE) build-ai-opencv &
	$(MAKE) build-ai-website-class &

	wait

.PHONY: build_run_api
build_run_api:
	@echo "Building API concurrently..."
	cd $(API_DIR) && \
	$(MAKE)

.PHONY: build_run_webapp
build_run_webapp:
	@echo "Building WebApp concurrently..."
	cd $(WEBAPP_DIR) && \
	$(MAKE)

# Build the WebApp, API, and AI concurrently
.PHONY: build-api-and-webapp
build-api-and-webapp:
	@echo "Building WebApp, API, and AI concurrently..."
	$(MAKE) build_run_api &
	$(MAKE) build_run_webapp &
	$(MAKE) build-ai-models &
	wait

# Optional: Add any cleanup or additional tasks here
