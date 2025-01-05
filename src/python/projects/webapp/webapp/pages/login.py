import reflex as rx
from webapp.webapp_interface.v1.schema.user import LoginForm

def login_page() -> rx.Component:
    return rx.center(
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
                            size="8",
                            as_="h1",
                            text_align="center",
                            width="100%",
                        ),
                    ),
                    rx.heading(
                        "Sign in to your account",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
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
                        value=LoginForm.email,
                        size="3",
                        width="100%",
                        on_change=LoginForm.change_email,  # Bind email input to state
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                        ),
                        rx.link(
                            "Forgot password?",
                            href="/reset-password",  # Example placeholder for reset link
                            size="3",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Enter your password",
                        value=LoginForm.password,
                        type="password",
                        size="3",
                        width="100%",
                        on_change=LoginForm.change_password,  # Bind password input to state
                    ),
                    spacing="2",
                    width="100%",
                ),
                # Conditional Retry or Sign-In logic
                rx.cond(
                    LoginForm.error_message,  # Check if an error occurred
                    rx.vstack(
                        rx.text(
                            LoginForm.error_message,  # Show the error message
                            color="red.500",
                            font_size="14px",
                            text_align="center",
                        ),
                        rx.button(
                            "Retry",  # Retry button for users to try again
                            size="3",
                            color_scheme="yellow",
                            width="100%",
                            on_click=LoginForm.reset_error_message,  # Reset state
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    # Else show the regular login button
                    rx.button(
                        "Sign in",
                        size="3",
                        width="100%",
                        color_scheme="blue",
                        on_click=LoginForm.login_button_click,  # Normal login flow
                    ),
                ),
                rx.center(
                    rx.text("New here?", size="3"),
                    rx.link("Sign up", href="/signup-page", size="3"),
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
