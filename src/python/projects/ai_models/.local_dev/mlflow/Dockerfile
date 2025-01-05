# mlflow/docker-compose.yml

FROM python:3.11-slim

# Set working directory
WORKDIR /mlflow

# Install dependencies
RUN pip install mlflow  boto3 psycopg2-binary cryptography pymysql

# Add this line in your docker-compose.yml

# Set environment variables


EXPOSE ${MLFLOW_PORT}
ENV MLFLOW_PORT=${MLFLOW_PORT}

ENV MLFLOW_TRACKING_URI=http://0.0.0.0:${MLFLOW_PORT}
ENV MLFLOW_S3_ENDPOINT_URL=${MLFLOW_S3_ENDPOINT_URL}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
# Command to run the MLflow server
CMD ["mlflow", "server", "--default-artifact-root", "s3://${MINIO_BUCKET_NAME}", "--host", "0.0.0.0", "--port", "${MLFLOW_PORT}"]
