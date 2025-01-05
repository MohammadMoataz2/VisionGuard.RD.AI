import reflex as rx

from webapp.webapp_interface.v1.schema.user import RegisterForm



def signup_page() -> rx.Component:
    return rx.center(  # Center the card in the middle of the screen
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="/VisionGuard.png",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.center(
                        rx.heading(
                            "Welcome to 🛡️ Vision Guard",
                            size="8",  # Large font size
                            as_="h1",
                            text_align="center",
                            width="100%",
                        ),
                    ),
                    rx.heading(
                        "Create an account",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                # Add the welcome text above the box
                rx.vstack(
                    rx.text(
                        "Username",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Omar Ahmad",
                        value=RegisterForm.username,
                        type="text",
                        size="3",
                        width="100%",
                        on_change=RegisterForm.change_username,  # Bind input to state
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email address",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="user@reflex.dev",
                        type="email",
                        value=RegisterForm.email,
                        size="3",
                        width="100%",
                        on_change=RegisterForm.change_email,  # Bind input to state
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Enter your password",
                        type="password",
                        value=RegisterForm.password,
                        size="3",
                        width="100%",
                        on_change=RegisterForm.change_password,  # Bind input to state
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.box(
                    rx.checkbox(
                        "Agree to Terms and Conditions",
                        default_checked=RegisterForm.agree_to_terms,

                        on_change=RegisterForm.change_agree,  # Bind checkbox to state
                        spacing="2",
                    ),
                    width="100%",
                ),
                # Display error message in red
                rx.text(
                    RegisterForm.error_message,  # Bind error message to text
                    color="red",  # Red color for error message
                    font_size="sm",  # Adjust font size as needed
                    margin_top="4",  # Add some spacing above the text
                ),
                rx.button(
                    "Register",
                    size="3",
                    width="100%",
                    on_click=RegisterForm.register_button_click,  # Bind button to function
                ),
                rx.center(
                    rx.text("Already registered?", size="3"),
                    rx.link("Sign in", href="/", size="3"),
                    opacity="0.8",
                    spacing="2",
                    direction="row",
                ),
                spacing="6",
                width="100%",
            ),
            size="4",
            max_width="28em",
            width="100%",
        ),
        width="100vw",  # Full viewport width
        height="100vh",  # Full viewport height
    )
