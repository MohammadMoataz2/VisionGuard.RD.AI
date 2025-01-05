import reflex as rx
from .webcam_feature import State
from webapp.webapp_interface.v1.schema.user import LoginForm
def custom_feature_page() -> rx.Component:
    return rx.cond(
        # Condition: Check if session is active
        LoginForm.session,
        # If True: Render the Custom Feature Page with logout button
        rx.container(
            rx.box(
                # Logout button in the top-right corner
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
                z_index="1000",  # Ensures it stays on top
            ),
            rx.vstack(
                rx.heading("🛡️ Vision Guard", font_size="70px", font_weight="bold"),
                # Center the heading
                rx.hstack(
                    rx.vstack(
                        rx.text("Age", font_weight="bold", font_size="20px"),  # Increase font size
                        rx.heading(LoginForm.age, font_size="24px"),  # Increase heading font size
                        rx.slider(
                            default_value=LoginForm.age,
                            on_value_commit=LoginForm.change_age,
                            size="lg",
                        ),
                        width="200px",  # Increase width for more space
                        align_items="center",
                    ),
                    rx.vstack(
                        rx.text("Gender", font_weight="bold", font_size="20px"),  # Increase font size
                        rx.select(
                            ["Man", "Woman"],
                            value=LoginForm.gender,
                            on_change=LoginForm.change_gender,
                            size="lg",
                            width="150px"
                        ),
                        align_items="center",
                    ),
                    rx.vstack(
                        rx.text("Emotion", font_weight="bold", font_size="20px"),  # Increase font size
                        rx.select(
                            ["angry", "fear", "neutral", "sad", "disgust", "happy", "surprise"],
                            value=LoginForm.emotion,
                            on_change=LoginForm.change_emotion,
                            size="lg",
                            width="150px"
                        ),
                        align_items="center",
                    ),
                    rx.vstack(
                        rx.text("Race", font_weight="bold", font_size="20px"),  # Increase font size
                        rx.select(
                            ["asian", "white", "middle eastern", "indian", "latino", "black"],
                            value=LoginForm.race,
                            on_change=LoginForm.change_race,
                            size="lg",
                            width="150px"
                        ),
                        align_items="center",
                    ),
                    spacing="5",  # Space between each input group
                    justify="center",
                    align_items="center",
                    margin_top="30px",
                    margin_bottom="50px"  # Increase margin bottom
                ),
                # Continue button centered below the form
                rx.button(
                    "Continue",
                    size="lg",
                    width="200px",
                    margin_top="30px",
                    font_size="20px",
                    on_click=LoginForm.handle_continue,
                    color_scheme="teal",  # You can adjust the color scheme
                    align_self="center",
                ),
                justify="center",
                align_items="center",
                padding_top="30px",  # 30px margin from top
                min_height="100vh",  # Full screen height
            ),
            justify="center",
            align_items="center"
        ),
        # If False: Render a message and button prompting the user to login
        rx.container(
            rx.vstack(
                # Centered message for unauthenticated users
                rx.text("You're not signed in to access this page, please log in.",
                        font_size="30px",
                        text_align="center",
                        color="red",
                        margin_bottom="20px"),
                # Login button
                rx.button(
                    "Go to Login Page",
                    on_click=rx.redirect("/"),
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