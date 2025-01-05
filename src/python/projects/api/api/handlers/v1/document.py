import logging
import uuid
from typing import List
from beanie import Document
from beanie.operators import In
from uuid import UUID
from enum import Enum
from fastapi import Body
from fastapi import APIRouter, HTTPException
from api.core import settings
from api.db.models import Document, User_Ad
from api.api_interface.v1.schema import (
SearchEngineResult,
    SearchEngineUserAttribute,
    SearchEngineUserAttributeOther,
    SearchEngineQueryBs4Google,
    SearchEngineUserResultQuery,
    SearchEngineResultQuery,
    SearchEngineUserQuery,
    Ad,
    AgeRange,
    AdContent,
    AttributesTargeting
)
import random

# Initialize the router and logger
router = APIRouter()
logger = logging.getLogger(settings.api_app_name)


@router.post("/create_ad")
async def create_ad(

):
    ad1 = User_Ad(
        ad_title="Fun-filled Musical Adventure to India, China, Japan and Many Other Asian Countries",
        category=["Music"],
        ad_content=AdContent(
            type="image",
            url="https://static.wixstatic.com/media/71157e_99fac0264b234eba97b0d4d63895dd21~mv2.jpg/v1/crop/x_0,y_2,w_900,h_896/fill/w_900,h_896,al_c,q_85,enc_avif,quality_auto/Asian%20Playground%20-%20WEB.jpg"
        ),
        attributes_targeting=AttributesTargeting(
            age_range=AgeRange(min=0, max=12),
            gender=["female", "male"],
            race=["asian", "indian"],
            emotion=["happy", "neutral", "surprise", "fear", "angry", "sad", "disgust"]
        ),
        location_targeting=[
            "India", "China", "Japan", "South Korea", "Indonesia", "Malaysia", "Singapore", "Thailand",
            "Philippines", "Vietnam", "Cambodia", "Myanmar"
        ],
        priority=1
    )

    await ad1.save()
    return ad1

# Endpoint to create a new user
@router.post("/create_user")
async def create_user(
    user_name: str,
    user_password: str,
    user_email: str,
    user_attributes: SearchEngineUserAttribute,
    user_attributes_other: SearchEngineUserAttributeOther,
):
    """
    Create a new user in the database with the provided attributes.

    Args:
        user_name (str): Name of the user.
        user_password (str): Password of the user.
        user_email (str): Email of the user.
        user_attributes (SearchEngineUserAttribute): User attributes.
        user_attributes_other (SearchEngineUserAttributeOther): Additional user attributes.

    Returns:
        Document: The created user document or a message indicating the email is already in use.
    """
    # Check if the email already exists in the database
    existing_user = await Document.find_one(Document.user_email == user_email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already in use")

    # Create a new user document
    user_obj = Document(
        user_name=user_name,
        user_password=user_password,
        user_email=user_email,
        user_attributes=user_attributes,
        user_attributes_other=user_attributes_other,
    )

    # Insert the new user into the database
    await user_obj.insert()
    logger.info(f"New user created: {user_obj}")

    return {"message": "User created successfully", "user": user_obj}

from .analyze import website_classification
# Endpoint to submit a search query
from fastapi_cache.decorator import cache
@router.post("/submit_query")
@cache()
async def submit_query(
    query: str = "",
    search_user_preferences: dict = {},
    user_email: str = "",
):
    print("search_user_preferences", search_user_preferences)
    """
    Submit a search query for a specific user and store the results.

    Args:
        query (str): The search query string.
        user_email (str): The email of the user.

    Returns:
        dict: A message and the query result.
    """
    # Fetch the user object from the database using the email
    classification_query = await website_classification(query)

    classification_query = classification_query.get("predictions", [{}])[0].get("text_label", "man")

    user_obj = await Document.find_one(Document.user_email == user_email)
    race = user_obj.user_attributes.race.name
    gender = user_obj.user_attributes.gender.name
    age = user_obj.user_attributes.age
    emotion = user_obj.user_attributes.emotion.name
    location = user_obj.user_attributes_other.location

    # Initialize SEARCH_OPTIMIZED flag and SEARCH_TERM_OPTIMIZED string
    SEARCH_OPTIMIZED = False
    SEARCH_TERM_OPTIMIZED = query

    # Iterate through the search preferences and adjust the search query based on active preferences
    for key, value in search_user_preferences.items():
        for preference, details in value.items():
            if details.get('active') == True:
                SEARCH_OPTIMIZED = True
                if preference == 'gender':
                    SEARCH_TERM_OPTIMIZED += f" for {gender.lower()}s"
                elif preference == 'race':
                    SEARCH_TERM_OPTIMIZED += f" in {race.lower()} culture"
                elif preference == 'age':
                    SEARCH_TERM_OPTIMIZED += f" for {age} year olds"
                elif preference == 'location':
                    SEARCH_TERM_OPTIMIZED += f" in {location.lower()}"



    # Optionally, you can print or log the optimized query
    print("Optimized Search Term:", SEARCH_TERM_OPTIMIZED)


    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")


    # Perform the search using the query
    search_result = SearchEngineQueryBs4Google(SEARCH_TERM=query,SEARCH_OPTIMIZED=SEARCH_OPTIMIZED,
                                               SEARCH_TERM_OPTIMIZED=SEARCH_TERM_OPTIMIZED ,
                                               SEARCH_USER_PREFERENCES=search_user_preferences["search_user_preferences"],
                                               SEARCH_CATEGORY=[classification_query])


    if not hasattr(user_obj, "user_preferences"):
        user_obj.user_preferences = {}

    for category in search_result.SEARCH_CATEGORY:
        if category in user_obj.user_preferences:
            user_obj.user_preferences[category] += 1
        else:
            user_obj.user_preferences[category] = 1

    # Create a query result object
    user_query_result = SearchEngineUserResultQuery(
        user_query=SearchEngineUserQuery(query_obj=search_result),
        result_query=SearchEngineResultQuery(query_result=search_result.search()),
    )

    # Add the result to the user's document
    if not hasattr(user_obj, "user_query_result"):
        user_obj.user_query_result = []

    # Update category value to "man" for each result in query_result
    for i, result in enumerate(user_query_result.result_query.query_result):
        print("Processing result:", result.title)

        # Call website_classification to get the category
        classification_response = await website_classification(result.title + " " + result.description)

        # Extract the text_label from the classification response
        text_label = classification_response.get("predictions", [{}])[0].get("text_label", "man")


        # Update the result directly in the query_result list
        user_query_result.result_query.query_result[i] = {
            "url": result.url,
            "title": result.title,
            "description": result.description,
            "categories": [text_label],  # Use the extracted text_label
        }


    user_preferences_active = search_user_preferences.get('search_user_preferences', {}).get('user_preferences', {}).get('active', False)

    if user_preferences_active:

        # Sort the user preferences by their values in descending order
        sorted_preferences = sorted(user_obj.user_preferences.items(), key=lambda x: x[1], reverse=True)

        # Sort the search results based on user preferences
        sorted_results = []
        categorized_results = {result["categories"][0]: result for result in user_query_result.result_query.query_result}

        for category, _ in sorted_preferences:
            if category in categorized_results:
                # Add results matching this category to the sorted list
                sorted_results.extend(
                    [result for result in user_query_result.result_query.query_result if category in result["categories"]]
                )

        # Add any remaining search results that don't match user preferences
        remaining_results = [
            result
            for result in user_query_result.result_query.query_result
            if result not in sorted_results
        ]
        sorted_results.extend(remaining_results)

        # Update the user query result with the sorted results
        user_query_result.result_query.query_result = sorted_results

    # Append the updated query result to the user's document
    user_obj.user_query_result.append(user_query_result)

    # Save the updated document
    await user_obj.save()

    # Prepare the updated result for the response
    new_user_query_result = [
        [result["title"], result["description"], result["url"], result["categories"][0]]
        for result in user_query_result.result_query.query_result
    ]

    return {"message": "Query submitted successfully", "result": new_user_query_result}

# Enum to specify the field to update
class UpdateField(str, Enum):
    username = "username"
    email = "email"

# Endpoint to update either the username or email
@router.put("/update_user_field")
async def update_user_field(
    id: str,
    current_password: str,
    field_to_update: UpdateField = UpdateField.username,
    new_value: str = "",
):
    """
    Update either the user's username or email if the provided password and ID are valid.

    Args:
        id (str): The UUID of the user.
        current_password (str): The current password of the user.
        field_to_update (UpdateField): The field to update ('username' or 'email').
        new_value (str): The new value for the specified field.

    Returns:
        dict: A success message if the update is successful.
    """
    # Validate the UUID
    try:
        user_id = UUID(id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Find the user in the database
    user_obj = await Document.find_one(Document.user_id == user_id)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the current password
    if user_obj.user_password != current_password:
        raise HTTPException(status_code=401, detail="Invalid password")

    # Update the specified field
    if field_to_update == UpdateField.username:
        user_obj.user_name = new_value
        logger.info(f"User ID {user_id} updated username to {new_value}")
    elif field_to_update == UpdateField.email:
        # Check if the email is already in use
        existing_user = await Document.find_one(Document.user_email == new_value)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email is already in use")
        user_obj.user_email = new_value
        logger.info(f"User ID {user_id} updated email to {new_value}")

    # Save the updated user document
    await user_obj.save()

    return {"message": f"User {field_to_update} updated successfully", "new_value": new_value}



@router.put("/update_password")
async def update_password(
    id: str,
    current_password: str,
    new_password: str = Body(..., description="The new password for the user"),
):
    """
    Update the user's password if the current password and user ID are valid.

    Args:
        id (str): The UUID of the user.
        current_password (str): The current password of the user.
        new_password (str): The new password to set.

    Returns:
        dict: A sucmcecss message if the update is successful.
    """
    # Validate the UUID
    try:
        user_id = UUID(id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Find the user in the database
    user_obj = await Document.find_one(Document.user_id == user_id)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the current password
    if user_obj.user_password != current_password:
        raise HTTPException(status_code=401, detail="Invalid current password")

    # Update the user's password
    user_obj.user_password = new_password
    logger.info(f"User ID {user_id} updated their password")

    # Save the updated user document
    await user_obj.save()

    return {"message": "Password updated successfully"}


@router.delete("/delete_user")
async def delete_user(
    id: str,
    current_password: str,
):
    """
    Delete a user from the database if the provided ID and current password are valid.

    Args:
        id (str): The UUID of the user.
        current_password (str): The current password of the user.

    Returns:
        dict: A success message if the user is successfully deleted.
    """
    # Validate the UUID
    try:
        user_id = UUID(id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # Find the user in the database
    user_obj = await Document.find_one(Document.user_id == user_id)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the current password
    if user_obj.user_password != current_password:
        raise HTTPException(status_code=401, detail="Invalid password")

    # Delete the user
    await user_obj.delete()
    logger.info(f"User ID {user_id} deleted successfully")

    return {"message": "User deleted successfully"}



@router.post("/login")
async def login(
    user_email: str,
    user_password: str,
):
    """
    Log the user in and return user data if credentials are valid.

    Args:
        user_email (str): The user's email.
        user_password (str): The user's password.

    Returns:
        dict: User data on successful login, or error message.
    """
    # Check if the user exists in the database
    user_obj = await Document.find_one(Document.user_email == user_email)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the password
    if user_obj.user_password != user_password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    # Return user data upon successful login
    user_data = {
        "user_name": user_obj.user_name,
        "user_email": user_obj.user_email,
        "user_attributes": user_obj.user_attributes,
        "user_attributes_other": user_obj.user_attributes_other,
    }

    return {"message": "Login successful", "user": user_data}




@router.post("/update_user_attributes")
async def update_user_attributes(
        user_email: str,
        current_password: str,
        user_attributes: dict = Body(None, description="Updated user attributes"),
        user_attributes_other: dict = Body(None, description="Updated additional user attributes"),
):
    """
    Update the user's attributes if the user ID and password are valid.

    Args:
        id (str): The UUID of the user.
        current_password (str): The current password of the user.
        user_attributes (dict): A dictionary of fields to update in 'user_attributes'.
        user_attributes_other (dict): A dictionary of fields to update in 'user_attributes_other'.

    Returns:
        dict: A success message if the update is successful.
    """
    # Validate the UUID

    # Find the user in the database
    user_obj = await Document.find_one(Document.user_email == user_email)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the current password
    if user_obj.user_password != current_password:
        raise HTTPException(status_code=401, detail="Invalid password")

    # Update user_attributes if provided
    if user_attributes:
        if not isinstance(user_obj.user_attributes, dict):
            user_obj.user_attributes = {}
        for key, value in user_attributes.items():
            user_obj.user_attributes[key] = value

    # Update user_attributes_other if provided
    if user_attributes_other:
        if not isinstance(user_obj.user_attributes_other, dict):
            user_obj.user_attributes_other = {}
        for key, value in user_attributes_other.items():
            user_obj.user_attributes_other[key] = value

    # Save the updated user document
    await user_obj.save()

    logger.info(f"User ID {user_email} updated their attributes: {user_attributes}, {user_attributes_other}")

    return {
        "message": "User attributes updated successfully",
        "user_attributes": user_obj.user_attributes,
        "user_attributes_other": user_obj.user_attributes_other,
    }


@router.post("/get_relevant_ads")
async def get_relevant_ads(
        user_attributes:dict
):
    user_age = user_attributes.get("age")
    user_gender = user_attributes.get("gender").lower()
    user_race = user_attributes.get("race").lower()
    user_emotion = user_attributes.get("emotion").lower()

    all_ads = await User_Ad.find_all().to_list()

    # Filter the ads in Python
    relevant_ads = [
        {
            "type": ad.ad_content.type,
            "url": ad.ad_content.url,
            "title": ad.ad_title,
            "categories": ad.category  # Adding categories
        }

        for ad in all_ads
        if ad.attributes_targeting.age_range.min <= int(user_age) <= ad.attributes_targeting.age_range.max
           and user_gender in map(str.lower, ad.attributes_targeting.gender)
           # and user_race in map(str.lower, ad.attributes_targeting.race)
           # and user_emotion in map(str.lower, ad.attributes_targeting.emotion)
    ]
    random.shuffle(relevant_ads)
    return   {
        "message": "User ads successfully",
        "ads": relevant_ads,
    }





@router.post("/update_user_preferences_result_page")
async def update_user_preferences_result_page(user_email: str, category: str):
    user_obj = await Document.find_one(Document.user_email == user_email)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")


    # Extract categories from the ad
    ad_categories =category

    # Update the user preferences
    user_preferences = user_obj.user_preferences


    if category in user_preferences:
        user_preferences[category] += 1
    else:
        user_preferences[category] = 1

    # Save the updated preferences to the user object
    user_obj.user_preferences = user_preferences
    await user_obj.save()

    logger.info(f"Updated preferences for user {user_email}: {user_preferences}")

    return {"message": "User preferences updated successfully", "updated_preferences": user_preferences}


@router.post("/update_user_preferences")
async def update_user_preferences(user_email: str, ad_url: str):
    """
    Update the user preferences based on the categories of the given ad.

    Args:
        user_email (str): Email of the user.
        ad_url (str): URL of the ad.

    Returns:
        dict: A message indicating success and the updated preferences.
    """
    # Fetch the user object from the database using the email
    user_obj = await Document.find_one(Document.user_email == user_email)

    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch the ad object from the database using the URL
    ad_obj = await User_Ad.find_one(User_Ad.ad_content.url == ad_url)

    if not ad_obj:
        raise HTTPException(status_code=404, detail="Ad not found")

    # Extract categories from the ad
    ad_categories = ad_obj.category

    # Update the user preferences
    user_preferences = user_obj.user_preferences

    for category in ad_categories:
        if category in user_preferences:
            user_preferences[category] += 1
        else:
            user_preferences[category] = 1

    # Save the updated preferences to the user object
    user_obj.user_preferences = user_preferences
    await user_obj.save()

    logger.info(f"Updated preferences for user {user_email}: {user_preferences}")

    return {"message": "User preferences updated successfully", "updated_preferences": user_preferences}
