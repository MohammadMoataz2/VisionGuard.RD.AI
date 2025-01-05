# Base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    libbz2-dev \
    libssl-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libffi-dev \
    liblzma-dev \
    ffmpeg \
    libsm6 \
    libxext6 && \
    pip install --no-cache-dir virtualenv && \
    curl https://pyenv.run | bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Environment Variables for Pyenv and MLflow
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="/root/.pyenv/bin:/root/.pyenv/shims:$PATH"

# Expose the server port
EXPOSE 5004

# Install Python version via Pyenv
RUN bash -c "source ~/.bashrc && pyenv install 3.11.11"

# Install Python dependencies
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt
# Copy application code
COPY . /app

# Set up to read environment variables from .env
COPY .env /app/.env

# Ensure .env is sourced when running the container
RUN echo "export $(cat /app/.env | xargs)" >> /root/.bashrc

# Command to serve the MLflow model using environment variables
CMD ["bash", "-c", "source ~/.bashrc && \
    mlflow models serve -m models:/$(echo $MODEL_NAME)@$(echo $MODEL_ALIAS) --port $MODEL_PORT"]

