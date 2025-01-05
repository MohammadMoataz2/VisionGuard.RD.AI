import reflex as rx
from webapp.webapp_interface.v1.schema.user import LoginForm
from functools import partial

suggestions_dict = {
    "apple": ["apple pie", "apple cider", "apple tree", "apple watch"],
    "banana": ["banana bread", "banana smoothie", "banana tree"],
    "cherry": ["cherry blossom", "cherry pie", "cherry tree"],
    "date": ["date palm", "date night", "dates nutrition"],
}

def create_button(label: int):
    return rx.button(
        f"{label}",
        bg="blue",
        color="white",
        margin="0.5em",
        padding="1em",
    )

@rx.page(on_load=LoginForm.retrieve_ads)
def search_engine_page() -> rx.Component:
    return rx.cond(
        LoginForm.session,
        rx.container(
            # Use a flex layout for the page content with left and right sections
            rx.flex(
                # Left section: Search Engine page
                rx.container(
                    rx.box(
                        rx.button(
                            "Logout",
                            on_click=LoginForm.logout,
                            font_size="15px",
                            padding="10px 15px",
                            background_color="red",
                            color="white",
                            border_radius="5px",
                        ),
                        rx.button(
                            "Welcome Page",
                            on_click=rx.redirect("/welcome-page"),
                            font_size="15px",
                            padding="10px 15px",
                            background_color="blue",
                            color="white",
                            border_radius="5px",
                            margin_left="10px",
                        ),
                        position="absolute",
                        top="20px",
                        right="20px",
                        z_index="1000",
                        display="flex",
                    ),
                    rx.vstack(
                        rx.heading("🛡️ Vision Guard", font_size="70px"),
                        justify="center",
                        align_items="center",
                        padding_top="20px",
                        min_height="15vh",
                    ),
                    rx.container(
                        rx.container(
                            rx.heading("🔍 Vision Guard Search", font_size="40px"),
                            justify="center",
                            align_items="center",
                            margin_bottom="20px",
                        ),
                        rx.flex(
                            rx.input(
                                rx.input.slot(
                                    rx.icon(tag="search"),
                                ),
                                placeholder="Search here...",
                                on_change=LoginForm.search_input_value,
                                width="80%",
                                border="1px solid #ccc",
                                border_radius="5px",
                                padding="0.5em",
                                font_size="1em",
                            ),
                            rx.button(
                                "Search",
                                width="20%",
                                bg="#272c31",
                                on_click=LoginForm.search_query,
                                color="white",
                                border_radius="5px",
                                padding="0.5em",
                                _hover={"bg": "darkblue"},
                                margin_left="1em",
                            ),
                            align_items="center",
                            direction="row",
                            gap="0.5em",
                            width="100%",
                        ),
                    ),
                    rx.container(
                        rx.cond(
                            LoginForm.box_appearance,
                            rx.box(
                                rx.vstack(
                                    rx.foreach(
                                        LoginForm.list_of_suggestions,
                                        lambda label: rx.button(
                                            f"{label}",
                                            variant="ghost",
                                            font_size="1.5em",
                                            padding="0.5em",
                                            on_click=partial(LoginForm.search_query, label),
                                            width="100%",
                                            _hover={"bg": "gray.200"},
                                            color="black",
                                            text_align="left",
                                            padding_left="1em",
                                        )
                                    ),
                                    padding="1em",
                                    gap="0.5em"
                                ),
                                border="1px solid #ccc",
                                border_radius="8px",
                                padding="1em",
                                box_shadow="lg",
                                bg="#b0bec5",
                                width="100%",
                            )
                        )
                    ),
                    justify="center",
                    align_items="center",
                    padding_top="10px",
                    margin_top="200px",
                ),
                # Right section: Image page
                rx.container(
                    image_page(),
                    width="50%",  # Occupy half of the page width
                    padding="10px",
                ),
            ),
            align_items="center",
            justify="center",
            spacing="5",
            min_height="85vh",
        ),
        rx.container(
            rx.vstack(
                rx.text(
                    "You're not signed in to access this page, please log in.",
                    font_size="30px",
                    text_align="center",
                    color="red",
                    margin_bottom="20px",
                ),
                rx.button(
                    "Go to Login Page",
                    on_click=rx.redirect("/"),
                    font_size="25px",
                    padding="15px 30px",
                    width="400px",
                    background_color="red",
                    color="white",
                    border_radius="10px",
                    box_shadow="0px 4px 6px rgba(0, 0, 0, 0.1)",
                ),
                justify="center",
                align_items="center",
                min_height="100vh",
                spacing="9",
            ),
        ),
    )


def image_page():
    image_url = "https://upload.wikimedia.org/wikipedia/en/1/1b/Adele_-_21.png"
    return rx.container(
        rx.text("Adele Greatest Hits Full Album 2024", font_size="xl", font_weight="bold"),
        rx.link(
            rx.image(src=image_url, alt="Adele Album", width="100%", height="auto"),
            href=image_url
        )
    )
