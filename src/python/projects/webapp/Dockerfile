# Use an official Python runtime as a parent image
FROM python:3.11-slim
RUN apt-get update && apt-get install -y unzip curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependenciess
RUN pip install --no-cache-dir -r requirements.txt


# Expose the ports the app runs on
EXPOSE $FRONTEND_PORT
EXPOSE $BACKEND_PORT

# Command to run the application
CMD ["reflex", "run"]