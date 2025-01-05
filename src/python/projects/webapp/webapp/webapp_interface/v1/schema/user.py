import reflex as rx
from webapp.core.settings import settings
import requests
from requests.auth import HTTPBasicAuth
import base64
# Standalone client function for sending requests
def send_request(request_body=None,params=None, tag=None, task_name=None):
    response = requests.post(
        f"{settings.API_CONN_STRING}{settings.API_V_STR}/{tag}/{task_name}",
        params=params,
        json=request_body,  # Request body
        auth=HTTPBasicAuth(settings.api_auth_username, settings.api_auth_password),
    )
    return response
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


class RegisterForm(rx.State):
    username: str = ""
    email: str = ""
    password: str = ""
    agree_to_terms: bool = False
    error_message: str = ""

    def on_load(self):
        self.reset()

    def change_username(self, val):
        self.username = val

    def change_email(self, val):
        self.email = val

    def change_password(self, val):
        self.password = val

    def change_agree(self, val):
        self.agree_to_terms = val

    def register_button_click(self):
        # Check if the user agreed to terms
        self.error_message=""
        if not self.agree_to_terms:
            self.error_message = "You must agree to the terms and conditions."
            return
        elif not self.username or not self.email or not self.password:
            self.error_message = "All fields are required."
            return

        self.error_message = ""

        query_params = {
            "user_name": self.username,
            "user_password": self.password,
            "user_email": self.email,
        }

        # Build JSON payload for the request
        build_json = {
            "user_attributes": {
                "default_attributes": True,
                "race": "asian",
                "gender": "Man",
                "age": 25,
                "emotion": "neutral",
            },
            "user_attributes_other": {"location": "New York"},
        }

        try:
            # Call the standalone function
            response = send_request(build_json, query_params, "document", "create_user")
            if response.status_code == 200:

                user_data = response.json().get("user", {})

                return rx.redirect("/")
            else:
                self.error_message = response.json().get("detail", "Registration failed.")

        except Exception as e:
            self.error_message = f"An error occurred: {str(e)}"


from pydantic import BaseModel
from typing import List, Dict

class AdContent(BaseModel):
    type: str
    url: str
    title: str
    categories: List[str]


class LoginForm(rx.State):
    email: str = ""
    password: str = ""
    error_message: str = ""
    username: str = ""
    default_attributes: bool = True
    age: int = 0
    gender: str = ""
    race: str = ""
    emotion: str = ""
    location: str = ""
    session: bool = False
    ads_result: List[Dict[str, str]]

    user_query: str = ""

    result_dict: list[list[str]] = [[]]
    search_bar_value: str = ""

    list_of_suggestions: list = []
    box_appearance: bool = False

    state: bool = False
    color: str = "red"
    status_text: str = "Face Not Detected"
    loading: bool = False
    progress_value: int = 0
    send: bool = True
    options_after: bool = False
    images: list = []
    analyze_face_state: bool = True
    face_analyze_result: dict = dict()
    analyze_options: bool = False

    loading_screen: bool = False

    user_preferences: Dict[str, Dict[str, str]] = {
        "gender": {
            "active": False,
            "color": "red"

        },
        "race":  {
            "active": False,
            "color": "red"

        },
        "age":  {
            "active": False,
            "color": "red"

        },
        "location":  {
            "active": False,
            "color": "red"

        },
        "user_preferences":  {
            "active": False,
            "color": "red"

        },
    }


    def toggle_user_preference(self, selected_values):

       if self.user_preferences[selected_values]["active"] == False:
            self.user_preferences[selected_values]["active"] = True
            self.user_preferences[selected_values]["color"] = "green"

       elif self.user_preferences[selected_values]["active"]  == True:
            self.user_preferences[selected_values]["active"]  = False
            self.user_preferences[selected_values]["color"] = "red"

       print(self.user_preferences)

    def get_color(self, value):

        if self.user_preferences[value]:
            return self.color_green
        else:
            return self.color_red

        print(self.color_red)
        print(value)

    def update_menu(self):
        # Print updated user preferences (this can be used for debugging)
        print(self.user_preferences)
    def track_result_click(self, category, url):
        print(f"Category: {category}, Redirecting to: {url}")
        # Redirecting to the URL

        response = send_request(params={"user_email": self.email, "category": category}, tag="document",
                            task_name="update_user_preferences_result_page")

    # Attributes for face analysis results
    def handle_adv_click(self, url):
        print(f"Redirecting to: {url}")

        response = send_request(params={"user_email": self.email, "ad_url":url}, tag="document", task_name="update_user_preferences")





    def handle_screenshot(self, img_data_uri: str):
        """Handle the webcam screenshot as a base64 URI and process it."""
        if img_data_uri and (self.progress_value < 100) and not self.face_analyze_result:
            base64_image = img_data_uri.split(",")[1]  # Remove "data:image/jpeg;base64,"
            image_bytes = base64.b64decode(base64_image)
            self.images.append(image_bytes)

            # Simulate face detection
            result = send_to_analyze(image_bytes, "analyze", "face_detection")
            if result["predictions"][0]["face"]:
                self.state = True
                self.color = "green"
                self.status_text = "Face Detected"
                self.progress_value += 3
            else:
                self.state = False
                self.color = "red"
                self.status_text = "Face Not Detected"

        # Once the progress reaches 100%, analyze face attributes
        if self.progress_value >= 100 and self.analyze_face_state:
            self.loading_screen = True
            self.face_analyze_result = send_to_analyze(self.images[0], "analyze", "face_analyze")
            self.loading_screen = False
            self.age = str(self.face_analyze_result["predictions"][0]["age"])
            gender_predictions = self.face_analyze_result["predictions"][0]["gender"]
            self.gender = max(gender_predictions, key=gender_predictions.get)  # Most likely gender
            self.race = self.face_analyze_result["predictions"][0]["race"]
            self.emotion = self.face_analyze_result["predictions"][0]["emotion"]

            # Update states to display analysis results
            self.analyze_face_state = False
            self.send = False
            self.state = True
            self.options_after = True
            self.analyze_options = True
            self.progress_value = 100


    def restart_page(self):
        """Reset the state for a new analysis."""
        self.analyze_face_state = True
        self.state = False
        self.color = "red"
        self.status_text = "Face Not Detected"
        self.loading = False
        self.progress_value = 0
        self.send = True
        self.options_after = False
        self.analyze_options = False
        self.images = []
        self.face_analyze_result = dict()
        self.analyze_face_state=True



    def search_input_value(self, value):
        self.user_query = value

        if len(value) > 0:
            self.box_appearance = True
        else:
            self.box_appearance = False


        import json
        import requests

        completion_query = value

        response = requests.get(f"http://google.com/complete/search?client=firefox&q={completion_query}")


        if value:

            self.list_of_suggestions = list(response.json()[1])
        else:
            self.list_of_suggestions = []


    def buttions_suguesstions(self):
        return self.list_of_suggestions




    def check_auth(self):
        if not self.session:
            return rx.redirect("/login-page/")


    def logout(self):
        self.session = False
        return rx.redirect("/")

    def on_load(self):
        self.reset_state()


    def change_age(self, val):
        self.age = val[0]

    def change_gender(self, val):
        self.gender = val
    def change_race(self, val):
        self.race = val
    def change_emotion(self, val):
        self.emotion = val
    def change_location(self, val):
        self.location = val

    def change_email(self, val):
        self.email = val

    def change_password(self, val):
        self.password = val

    def change_error_message(self, val):
        self.error_message = val


    def reset_state(self):
        """Reset the state to clear error messages for retrying login."""
        self.email = ""
        self.password = ""
        self.error_message = ""

    def reset_error_message(self):
        self.error_message = ""


    def search_query(self, value = None):

        if value is not None:
            self.user_query = value
        print("This is the ")

        query_params = {
            "query": self.user_query,
            "user_email": self.email,
        }

        response = send_request(
            request_body={
                "search_user_preferences": self.user_preferences,

            },
            params=query_params,
            tag="document",
            task_name="submit_query",
        )


        if response.status_code == 200:
            self.result_dict = response.json()["result"]
            return rx.redirect("/search-engine-result-page/")

    @rx.event
    def retrieve_ads(self):
        user_attributes = {
            "age":self.age,
            "gender":self.gender,
            "race":self.race,
            "emotion":self.emotion,
        }

        response = send_request(
            request_body=user_attributes,

            tag="document",
            task_name="get_relevant_ads",

        )
        self.ads_result = response.json()["ads"]

    def handle_continue(self):
        # Collect user attributes to send to the update endpoint
        user_attributes = {
            "default_attributes": False,
            "race": self.race,
            "gender": self.gender,
            "age": int(self.age),  # Ensure the age is an integer
            "emotion": self.emotion,
        }
        user_attributes_other = {
            "location": self.location,
        }

        # Build query parameters for authentication
        query_params = {
            "user_email": self.email,
            "current_password": self.password,
        }

        try:
            # Send the request to update user attributes
            response = send_request(
                request_body={
                    "user_attributes": user_attributes,
                    "user_attributes_other": user_attributes_other,
                },
                params=query_params,
                tag="document",
                task_name="update_user_attributes",
            )


            if response.status_code == 200:
                # If successful, redirect to the search engine page
                return rx.redirect("/search-engine-page/")
            else:
                # Handle failure by showing error details
                self.error_message = response.json().get("detail", "Failed to update attributes.")
        except Exception as e:
            # Handle any other exceptions
            self.error_message = f"An error occurred: {str(e)}"

    def login_button_click(self):
        # Check if email and password are provided
        if not self.email or not self.password:
            self.error_message = "Email and password are required."
            return

        self.error_message = ""

        query_params = {
            "user_email": self.email,
            "user_password": self.password,
        }

        try:
            # Call the standalone function
            response = send_request(None, query_params, "document", "login")
            if response.status_code == 200:
                # Parse the JSON response
                response_data = response.json()
                user_data = response_data.get("user", {})

                # Assign response data to the LoginForm attributes
                self.username = user_data.get("user_name", "")
                self.email = user_data.get("user_email", "")
                self.default_attributes = user_data.get("user_attributes", {}).get("default_attributes", True)
                self.race = user_data.get("user_attributes", {}).get("race", "")
                self.gender = user_data.get("user_attributes", {}).get("gender", "")
                self.age = user_data.get("user_attributes", {}).get("age", 0)
                self.emotion = user_data.get("user_attributes", {}).get("emotion", "")
                self.location = user_data.get("user_attributes_other", {}).get("location", "")

                self.session = True
                LoginForm.retrieve_ads()
                if self.default_attributes:
                    return rx.redirect("/welcome-page")
                else:
                    return rx.redirect("/search-engine-page/")
                # Redirect to the dashboard page or homepage
            else:
                # Handle login failure and extract error message
                self.error_message = response.json().get("detail", "Invalid email or password.")

        except Exception as e:
            self.error_message = f"An error occurred: {str(e)}"
