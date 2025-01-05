import reflex as rx
import reflex_webcam as webcam
import base64
from .api_connector import send_to_analyze
from webapp.webapp_interface.v1.schema.user import LoginForm

# Webcam reference in the DOM
WEBCAM_REF = "webcam"







class State(rx.State):
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

    # Attributes for face analysis results
    age: str = "20"
    gender: str = "Man"
    emotion: str = "happy"
    race: str = "asian"

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
        self.options_after: bool = False

    def change_gender(self, gender):
        self.gender = gender

    def change_age(self, value):
        self.age = value[0]


    def change_emotion(self,emotion):
        self.emotion = emotion
    def change_race(self,race):
        self.race = race


def webcam_display_component(ref: str) -> rx.Component:
    """Component to display the webcam feed."""
    return rx.box(
        webcam.webcam(id=ref),
    )


def webcam_page() -> rx.Component:
    """Main page component with webcam and status display."""
    return rx.cond(
        # Session validation: Display webcam page if session is valid
        LoginForm.session,
        # If True: Render the webcam page with logout button
        rx.container(
            # Logout button in the top-right corner
            rx.box(
                rx.button(
                    "Logout",
                    on_click=LoginForm.logout,  # Redirect to login page after logout
                    font_size="15px",
                    padding="10px 15px",
                    background_color="red",
                    color="white",
                    border_radius="5px",
                ),
                position="absolute",
                top="20px",
                right="20px",
                z_index="1000",  # Ensures logout button stays on top
            ),
            # Page content
            rx.vstack(
                rx.heading("🛡️ Vision Guard", font_size="70px"),
                justify="start",
                align_items="center",
                padding_top="50px",
                min_height="10vh",
            ),
            rx.center(
                webcam_display_component(WEBCAM_REF),
                padding_top="3em",
            ),
            rx.center(
                rx.box(
                    rx.text(LoginForm.status_text, color="white", font_size="20px"),
                    background=LoginForm.color,
                    width="100%",
                    height="50px",
                    align_items="center",
                    justify_content="center",
                    display="flex",
                    margin_top="10px",
                )
            ),
            rx.center(
                rx.progress(value=LoginForm.progress_value, max=100, width="50%", height="20px", color="blue"),
                padding_top="10px",
            ),
            # Invisible button that triggers screenshot capture
            rx.button(
                "",
                on_click=webcam.upload_screenshot(
                    ref=WEBCAM_REF,
                    handler=LoginForm.handle_screenshot,
                ),
                id="update-trigger",
                style={"display": "none"},
            ),
            rx.cond(
                LoginForm.send,
                rx.script(
                    """
                    setInterval(function() {
                        document.getElementById("update-trigger").click();
                    }, 100);
                    """
                ),
            ),
            # Display analyzed attributes with labels above each input
            rx.cond(
                LoginForm.analyze_options,
                rx.hstack(
                    rx.vstack(
                        rx.text("Age", font_weight="bold", font_size="20px"),  # Increase font size
                        rx.heading(LoginForm.age, font_size="24px"),
                        rx.slider(
                            default_value=LoginForm.age,
                            on_value_commit=LoginForm.change_age,
                            size="lg",
                        ),
                        width="200px",
                        align_items="center",
                    ),
                    rx.vstack(
                        rx.text("Gender", font_weight="bold", font_size="20px"),
                        rx.select(
                            ["Man", "Woman", "Prefer not to say"],
                            value=LoginForm.gender,
                            on_change=LoginForm.change_gender,
                            size="lg",
                            width="150px"
                        ),
                        align_items="center",
                    ),
                    rx.vstack(
                        rx.text("Emotion", font_weight="bold", font_size="20px"),
                        rx.select(
                            ["angry", "fear", "neutral", "sad", "disgust", "happy", "surprise", "Prefer not to say"],
                            value=LoginForm.emotion,
                            on_change=LoginForm.change_emotion,
                            size="lg",
                            width="150px",
                        ),
                        align_items="center",
                    ),
                    rx.vstack(
                        rx.text("Race", font_weight="bold", font_size="20px"),
                        rx.select(
                            ["asian", "white", "middle eastern", "indian", "latino", "black", "Prefer not to say"],
                            value=LoginForm.race,
                            on_change=LoginForm.change_race,
                            size="lg",
                            width="150px",
                        ),
                        align_items="center",
                    ),
                    spacing="5",  # Space between each input group
                    justify="center",
                    align_items="center",
                    margin_top="30px",
                    margin_bottom="50px"
                ),
            ),
            # Buttons for actions after analysis
            rx.cond(
                LoginForm.options_after,
                rx.hstack(
                    rx.button(
                        "Continue",
                        on_click=LoginForm.handle_continue(),
                        font_size="20px",
                        padding="10px 20px",
                    ),
                    rx.button(
                        "Retry",
                        on_click=LoginForm.restart_page,
                        font_size="20px",
                        padding="10px 20px",
                    ),
                    margin_top="20px",
                    margin_bottom="70px",
                    spacing="5",
                    justify="center",
                    align_items="center",
                ),
            )
        ),
        # If False: Render a login prompt message
        rx.container(
            rx.vstack(
                # Centered message for unauthenticated users
                rx.text(
                    "You're not signed in to access this page, please log in.",
                    font_size="30px",
                    text_align="center",
                    color="red",
                    margin_bottom="20px",
                ),
                # Login button
                rx.button(
                    "Go to Login Page",
                    on_click=rx.redirect("/"),  # Redirect to the login page
                    font_size="25px",
                    padding="15px 30px",
                    width="400px",  # Larger width for visual emphasis
                    background_color="red",
                    color="white",
                    border_radius="10px",
                    box_shadow="0px 4px 6px rgba(0, 0, 0, 0.1)",  # Add shadow for prominence
                ),
                justify="center",
                align_items="center",
                min_height="100vh",  # Vertically center the content
                spacing="9",  # Space between message and button
            ),
        ),
    )

