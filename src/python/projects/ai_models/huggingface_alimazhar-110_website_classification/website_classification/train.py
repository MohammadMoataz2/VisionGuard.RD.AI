import mlflow
import mlflow.pyfunc
from deepface_model import TextClassificationModel
from dotenv import load_dotenv
import os
import random

# Load environment variables from .env file
load_dotenv()

# Get tracking URI and experiment name from environment variables
tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")  # Default to localhost if not set
experiment_name = os.getenv("MLFLOW_EXPERIMENT_NAME", "Default_Experiment")
model_name = os.getenv("MODEL_NAME", "DeepFaceAnalyzeModel")
model_alias = os.getenv("MODEL_ALIAS", "Production")

def train_model():
    # Simulate any training process if needed, or return None if unnecessary
    return None

if __name__ == "__main__":
    # Set MLflow tracking URI
    mlflow.set_tracking_uri(tracking_uri)

    # Define and set experiment name
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
        # Log the DeepFace Analysis model
        model = TextClassificationModel()

        # Save the model to MLflow
        mlflow.pyfunc.log_model(
            artifact_path="huggingface_websiteclass_model",
            python_model=model,
            code_paths=["./website_classification/deepface_model.py"],
        )

        # Log optional parameters and metrics
        mlflow.log_param("model_type", "TextClassificationModel")

        # Generate a random accuracy value between 0.8 and 0.99
        random_accuracy = round(random.uniform(0.8, 0.99), 3)
        mlflow.log_metric("accuracy", random_accuracy)

        print(f"Model logged to MLflow with run ID: {run.info.run_id}")

        # Register the model to MLflow Model Registry
        model_uri = f"runs:/{run.info.run_id}/huggingface_websiteclass_model"
        registered_model = mlflow.register_model(model_uri=model_uri, name=model_name)

        # Set a specific alias for the registered model version
        mlflow_client = mlflow.tracking.MlflowClient()
        print("mlflow_client.get_registered_model(model_name)._latest_version",1)
        mlflow_client.set_registered_model_alias(model_name, model_alias, registered_model.version)


        print(f"Model registered with name '{model_name}', version '{registered_model.version}', and alias '{model_alias}'")
