# Root Makefile

.PHONY: all mlflow mysql minio start

include .env
export

# Default target to start all services
all: start

# Start all services
start: mlflow mysql minio

# Start MLflow service
mlflow:
	$(MAKE) -C mlflow up

# Start MySQL service
mysql:
	$(MAKE) -C mysql up

# Start Minio service
minio:
	$(MAKE) -C minio up

# Stop all services
stop: mlflow-stop mysql-stop minio-stop
	@echo "All services stopped."

# Stop MLflow service
mlflow-stop:
	$(MAKE) -C mlflow down

# Stop MySQL service
mysql-stop:
	$(MAKE) -C mysql down

# Stop Minio service
minio-stop:
	$(MAKE) -C minio down

