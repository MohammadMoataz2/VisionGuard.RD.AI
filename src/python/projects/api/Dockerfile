# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . /app

# Install python-dotenv to load environment variables
RUN pip install python-dotenv

# Expose the port FastAPI will run on
EXPOSE ${API_PORT}
ENV API_PORT=${API_PORT}

# Set the environment variable for FastAPI to read .env file
ENV PYTHONPATH=/app

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
