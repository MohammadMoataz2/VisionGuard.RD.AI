# Declare phony targets to prevent conflicts with filenames
.PHONY: build-deepface build-opencv build-local-dev build-huggingface-websiteclass
all: build-local-dev build-deepface build-opencv build-huggingface-websiteclass
# DeepFace Project Section
build-deepface:
	@echo "Building DeepFace Docker image..."
	$(MAKE) -C deepface_face_analyze

# OpenCV Project Section
build-opencv:
	@echo "Building OpenCV Docker image..."
	$(MAKE) -C opencv_face_detection

build-huggingface-websiteclass:
	@echo "Building website class Docker image..."
	$(MAKE) -C huggingface_alimazhar-110_website_classification

# Local Development Section
build-local-dev:
	@echo "Building Local Development Docker images..."
	$(MAKE) -C .local_dev
