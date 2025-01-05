import mlflow.pyfunc
import pandas as pd
from transformers import pipeline


class TextClassificationModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        # Initialize the Hugging Face text classification pipeline inside the class
        self.text_pipe = pipeline("text-classification", model="alimazhar-110/website_classification")

    def predict(self, context, model_input: pd.DataFrame):
        # Assuming 'text' column contains the input text
        text_input = model_input["text"].iloc[0]

        # Use the Hugging Face model to classify the text
        text_classification = self.text_pipe(text_input)

        # Extract the classification result
        result = {
            "text_label": text_classification[0]["label"],
            "text_score": text_classification[0]["score"]
        }

        return pd.DataFrame([result])
