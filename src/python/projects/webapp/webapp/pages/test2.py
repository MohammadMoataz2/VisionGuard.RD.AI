import reflex as rx
from webapp.webapp_interface.v1.schema.user import LoginForm
from functools import partial
from reflex.vars import Var



def get_color(preference):
    if LoginForm.user_preferences[preference]:
        return "green"
    else:
        return "red"

@rx.page(on_load=LoginForm.retrieve_ads, route="search-engine-page")
def image_page():
    try:
        return rx.cond(
            LoginForm.session,
            rx.flex(
                # Top flex container
                rx.flex(
                    rx.container(
                        rx.vstack(
        rx.text("Please rate the relevance of the ads", font_size="lg", font_weight="bold", text_align="center", margin_bottom="20px"),

                            # Display the feedback buttons (thumbs up and down)
                            rx.hstack(
                                rx.button("👍", width="40px", height="40px", border_radius="20px", background="green", color="white", font_size="lg"),
                                rx.button("👎", width="40px", height="40px", border_radius="20px", background="red", color="white", font_size="lg"),
                            ),
        rx.text("Relevant Ads", font_size="md", font_weight="medium", color="gray", cursor="pointer", margin_top="10px"),
        margin_top="20px",

                        ),
                        width="20%",
                        height="20%px"
                    ),
                    rx.container(
                        rx.vstack(
                            rx.heading("🛡️ Vision Guard", font_size="70px"),
                            justify="center",
                            align_items="center",
                            padding_top="20px",
                            min_height="15vh",
                        ),
                        width="60%",
                        height="150px"
                    ),
                    rx.container(
                        rx.box(
                            rx.button(
                                "Dashboard and Control",
                                on_click=LoginForm.logout,
                                font_size="15px",
                                padding="10px 15px",
                                background_color="gray",
                                color="white",
                                border_radius="5px",
                                margin_right="10px",

                            ),

                            rx.button(
                                "Welcome Page",
                                on_click=rx.redirect("/welcome-page"),
                                font_size="15px",
                                padding="10px 15px",
                                background_color="blue",
                                color="white",
                                border_radius="5px",
                                margin_right="10px",
                            ),

                            rx.button(
                                "Logout",
                                on_click=LoginForm.logout,
                                font_size="15px",
                                padding="10px 15px",
                                background_color="red",
                                color="white",
                                border_radius="5px",
                            ),




                            position="absolute",
                            top="20px",
                            right="20px",
                            z_index="1000",
                            display="flex",
                        ),
                        width="20%",
                        height="150px"
                    ),
                    direction="row",
                    width="100%",
                    height="150px",
                ),
                # Middle flex container
                rx.flex(
                    rx.container(
                        width="20%",
                        height="200px"
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

                            rx.menu.root(
                                rx.menu.trigger(rx.button("Optimize Query Options", variant="soft")),
                                rx.menu.content(
                                    # Add on_click handlers to send the string value
                                    rx.menu.item(f"gender",
                                                 on_click=lambda: LoginForm.toggle_user_preference("gender"),
                                                 bg=LoginForm.user_preferences["gender"]["color"]
                                                ,margin_y = "5px"
                                                 # Change color based on the preference value
                                                 ),
                                    rx.menu.item("race", on_click=lambda: LoginForm.toggle_user_preference("race"),
                                                 bg=LoginForm.user_preferences["race"]["color"]
                                                 , margin_y="5px"
                                                 ),
                                    rx.menu.item("age", on_click=lambda: LoginForm.toggle_user_preference("age"),
                                                 bg=LoginForm.user_preferences["age"]["color"]
                                                 , margin_y="5px"
                                                 ),
                                    rx.menu.item("location", on_click=lambda: LoginForm.toggle_user_preference("location"),
                                                 bg=LoginForm.user_preferences["location"]["color"]
                                                 , margin_y="5px"
                                                 ),
                                    rx.menu.item("user_preferences", on_click=lambda: LoginForm.toggle_user_preference("user_preferences"),
                                                 bg=LoginForm.user_preferences["user_preferences"]["color"]
                                                 , margin_y="5px"
                                                 ),

                                )
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
                        width="60%",
                        height="200px"
                    ),
                    rx.container(
                        width="20%",
                        height="200px"
                    ),
                    direction="row",
                    width="100%",
                    height="200px",
                    margin_y="10px",
                ),
                # Bottom flex container
                rx.flex(
                    rx.container(
                        rx.link(
                            rx.text(LoginForm.ads_result[1]["title"], font_size="15px", font_weight="bold"),
                            rx.image(
                                src=LoginForm.ads_result[1]["url"],
                                alt="Adele Album",
                                width="300px",
                                height="200px",
                            ),
                            href=LoginForm.ads_result[1]["url"],
                            on_click=lambda: LoginForm.handle_adv_click(LoginForm.ads_result[1]["url"]),
                            # This calls the handle_adv_click function
                        ),
                        width="20%",
                        height="90%",
                        align_items="flex-end",
                        justify_content="flex-end",
                        direction="row",
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
                        ),
                        width="60%",
                        height="300px"
                    ),
                    rx.container(
                        rx.link(
                            rx.text(LoginForm.ads_result[0]["title"], font_size="15px", font_weight="bold"),
                            rx.image(
                                src=LoginForm.ads_result[0]["url"],
                                alt="Adele Album",
                                width="300px",
                                height="200px",
                            ),
                            href=LoginForm.ads_result[0]["url"],
                            on_click=lambda: LoginForm.handle_adv_click(LoginForm.ads_result[0]["url"]),
                            # This calls the handle_adv_click function
                        ),
                        width="20%",
                        height="90%",
                        align_items="flex-end",
                        justify_content="flex-end",
                        direction="row",
                    ),
                    direction="row",
                    width="100%",
                    height="300px",
                    margin_y="10px",
                ),
                direction="column",
                width="100%",
                height="100%",
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
    except Exception as e:
        # Reload the page in case of an error
        return rx.js_eval("window.location.reload()")
