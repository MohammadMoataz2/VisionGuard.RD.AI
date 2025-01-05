import logging
import uuid
from typing import List
from uuid import UUID
from enum import Enum
from fastapi import Body
from fastapi import APIRouter, HTTPException
from api.core import settings
import base64
import json
import requests

from fastapi import APIRouter, File, UploadFile
import base64
import requests
from api.core.settings import settings



# Initialize the router and logger
router = APIRouter()
logger = logging.getLogger(settings.api_app_name)




async def send_to_analyze(file: UploadFile, conn_str):
    # Read the file content as bytes
    image_bytes = await file.read()

    # Encode the image bytes to Base64 for transmission
    base64_encoded_image = base64.b64encode(image_bytes).decode('utf-8')

    payload = {
        "dataframe_split": {
            "columns": ["image_bytes"],
            "data": [[base64_encoded_image]]
        }
    }

    # Send POST request to the MLflow model server
    response = requests.post(conn_str, json=payload)

    # Parse and return response as JSON
    return response.json()


@router.post("/face_detection")
async def face_detection(file: UploadFile = File(...)):
    return await send_to_analyze(file,settings.FACE_DETECTION_CONN_STR)  # Port for face detection

@router.post("/face_analyze")
async def face_analyze(file: UploadFile = File(...)):
    return await send_to_analyze(file, settings.FACE_ANALYZE_CONN_STR)  # Port for face analysis




async def send_to_analyze_text(text: str, conn_str):
    # Read the file content as bytes

    payload = {
        "dataframe_split": {
            "columns": ["text"],
            "data": [[text]]
        }
    }

    # Send POST request to the MLflow model server
    response = requests.post(conn_str, json=payload)

    # Parse and return response as JSON
    return response.json()


@router.post("/website-class")
async def website_classification(text: str):
    return await send_to_analyze_text(text, settings.WEBSITE_CLASS_CONN_STR)  # Port for face analysis
