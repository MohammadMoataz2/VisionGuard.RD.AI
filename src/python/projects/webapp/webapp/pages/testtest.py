import reflex as rx
from webapp.webapp_interface.v1.schema.user import LoginForm

@rx.page(on_load=LoginForm.retrieve_ads,route="search-engine-result-page/")
def index() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.container(
                rx.button(
                    "Return To Search Page",
                    on_click=rx.redirect("/search-engine-page/"),  # Redirect to welcome page
                    font_size="15px",
                    padding="10px 15px",
                    background_color="#b0bec5",
                    color="black",
                    border_radius="5px",
                    margin_left="10px",  # Add space between Logout and Welcome Page buttons
                ),

                rx.vstack(
                    rx.text("Please rate the relevance of the Result", font_size="lg", font_weight="bold",
                            text_align="center", margin_bottom="20px"),

                    # Display the feedback buttons (thumbs up and down)
                    rx.hstack(
                        rx.button("👍", width="40px", height="40px", border_radius="20px", background="green",
                                  color="white", font_size="lg"),
                        rx.button("👎", width="40px", height="40px", border_radius="20px", background="red",
                                  color="white", font_size="lg"),
                    ),
                    rx.text("Relevant Result", font_size="md", font_weight="medium", color="gray", cursor="pointer",
                            margin_top="10px"),
                    margin_top="20px",

                ),

                width="50%",
            ),
            rx.container(
                rx.vstack(
                    rx.heading("🛡️ Vision Guard", font_size="70px"),
                    justify="center",
                    align_items="center",
                    padding_top="20px",  # Adjust padding to position at the top center
                    min_height="15vh",  # Adjust height for top positioning
                ),
                width="110%",
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
                    z_index="1000",  # Ensures the buttons stay on top
                    display="flex",  # Align buttons horizontally
                ),

                width="50%",
            ),
            width="100%",
        ),

        rx.flex(
            rx.container(

                rx.scroll_area(
                    rx.vstack(
                        rx.foreach(
                            LoginForm.result_dict,
                            lambda result: rx.card(
                                rx.link(
                                    rx.flex(
                                        rx.avatar(src="/reflex_banner.png"),
                                        # Optional: Replace with a relevant image if needed
                                        rx.box(
                                            rx.heading(result[0], size="md"),  # Dynamically set the title
                                            rx.badge(
                                                result[3],  # Dynamically set the category
                                                color_scheme="blue",  # Choose a color scheme for the badge
                                                margin_bottom="0.5em",
                                                font_size="sm",
                                            ),
                                            rx.text(result[1]),  # Dynamically set the description
                                        ),
                                        spacing="2",
                                    ),
                                    href=result[2],  # Dynamically set the href
                                    is_external=True,  # Opens the link in a new tab
                                    on_click=lambda: LoginForm.track_result_click(result[3], result[2]),
                                    # Calls track_result_click with category and URL
                                ),
                                as_child=True,
                                width="90%",
                                margin="1em 0",  # Adds spacing between cards
                            ),
                        ),

                    ),
                    type="always",
                    scrollbars="vertical",
                    width="100%",
                    height="80%",
                    margin_y="3em",
                    margin_bottom="3em",
                ),

                         width="110%",
                         height="80%",),
            rx.container(

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
                        rx.link(
                            rx.text(LoginForm.ads_result[2]["title"], font_size="15px", font_weight="bold"),
                            rx.image(
                                src=LoginForm.ads_result[2]["url"],
                                alt="Adele Album",
                                width="300px",
                                height="200px",
                            ),
                            is_external=True,
                            href=LoginForm.ads_result[2]["url"],
                            on_click=lambda: LoginForm.handle_adv_click(LoginForm.ads_result[2]["url"]),
                            # This calls the handle_adv_click function
                        ),
                        width="20%",
                        height="90%",
                        align_items="flex-end",
                        justify_content="flex-end",
                        direction="row",
                    )

                ),

                         width="100%",
                         height="80%",),

            width="100%",
            height="100%",

        ),


        align_items="flex-start",
        margin_left="20px",
        height="300px"



    )



