import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch","https://twitch.tv"),
        link_button("Instagram", "https://instagram.com"),
        link_button("Youtube", "https://youtube.com"),
        link_button("Otro boton", "https://google.com"),
        width="100%"
    )