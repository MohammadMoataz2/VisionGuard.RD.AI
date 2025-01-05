import reflex as rx
from rxconfig import config
from PIL import Image

from .pages.webcam_feature import webcam_page
from .pages.custome_feature import custom_feature_page
from .pages.search_engine import search_engine_page
from .pages.register import signup_page
from .pages.login import login_page
from webapp.webapp_interface.v1.schema.user import LoginForm


@rx.page(route="/protected", on_load=LoginForm.check_auth)
def welcome_page() -> rx.Component:
    return rx.cond(
        # Condition: Check if session is active
        LoginForm.session,
        # If True: Render full Welcome Page with logout button
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
                z_index="1000",  # Ensures it stays on top
            ),
            # Top heading
            rx.vstack(
                rx.heading("🛡️ Vision Guard", font_size="70px", text_align="center"),
                justify="start",
                align_items="center",
                padding_top="50px",
                min_height="10vh",
            ),
            # Centered content
            rx.vstack(
                rx.text(f"Welcome to Vision Guard {LoginForm.username}!", font_size="30px", text_align="center"),
                rx.text(
                    "This is an AI application designed to leverage your webcam "
                    "and advanced algorithms to analyze and collect features.",
                    font_size="20px",
                    text_align="center",
                ),
                # Buttons aligned side by side
                rx.hstack(
                    rx.button(
                        "Go to Webcam Page",
                        on_click=rx.redirect("/webcam-page"),
                        font_size="20px",
                        padding="10px 20px",
                        width="300px",  # Fixed width for uniform buttons
                        background_color="blue",
                        color="white",
                        border_radius="5px",
                    ),
                    rx.button(
                        "Go to Custom Feature Page",
                        on_click=rx.redirect("/custom-feature-page"),
                        font_size="20px",
                        padding="10px 20px",
                        width="300px",  # Fixed width for uniform buttons
                        background_color="green",
                        color="white",
                        border_radius="5px",
                    ),
                    spacing="5",  # Space between buttons
                    justify="center",
                ),
                align_items="center",
                spacing="5",
                justify="center",
                min_height="75vh",
            ),
        ),
        # If False: Show a centered message and button redirecting to the login page
        rx.container(
            rx.vstack(
                # Centered message
                rx.text("You're not signed in to access this page, please log in.",
                        font_size="30px",
                        text_align="center",
                        color="red",
                        margin_bottom="20px"),
                # Redirect button
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
                spacing="9",  # Add spacing between message and button
            ),
        ),
    )



# Initialize and configure the app
app = rx.App()

# Add pages with their routes
app.add_page(welcome_page, route="/welcome-page")
app.add_page(webcam_page, route="/webcam-page")
app.add_page(custom_feature_page, route="/custom-feature-page")
# app.add_page(search_engine_page, route="/search-engine-page")
app.add_page(signup_page(), route="/signup-page")
app.add_page(login_page(), route="/")
from .pages.testtest import index
from .pages.test2 import image_page
app.add_page(image_page, route="/search-engine-page")
app.add_page(index, route="/search-engine-result-page/")



# Run the app
if __name__ == "__main__":
    app.run()