import base64
import json
import requests
from requests.auth import HTTPBasicAuth
from webapp.core.settings import settings

def send_to_analyze(encoded_image, tag, task_name):
    # Convert image bytes to base64
    base64_encoded_image = base64.b64encode(encoded_image).decode('utf-8')

    # Create the payload in dataframe_split format
    files = {
        'file': ('image.jpg', encoded_image, 'image/jpeg')  # Sending the image file as bytes
    }

    response = requests.post(
        f"{settings.API_CONN_STRING}{settings.API_V_STR}/{tag}/{task_name}",
            files=files,
        auth=HTTPBasicAuth(settings.api_auth_username, settings.api_auth_password)  # Include the HTTP Basic Authentication
    )

    # Parse the response as JSON
    response_json = response.json()

    return response_json


