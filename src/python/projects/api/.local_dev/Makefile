# Root Makefile

.PHONY: all mongodb redis start

include .env
export

# Default target to start all services
all: start

# Start all services
start: mongodb redis

# Start MongoDB service
mongodb:
	$(MAKE) -C mongodb up

# Start Redis service
redis:
	$(MAKE) -C redis up

# Stop all services
stop: mongodb-stop redis-stop
	@echo "All services stopped."

# Stop MongoDB service
mongodb-stop:
	$(MAKE) -C mongodb down

# Stop Redis service
redis-stop:
	$(MAKE) -C redis down
