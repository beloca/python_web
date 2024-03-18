import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
def links() -> rx.Component:
    return rx.vstack(
        title("Primer reflex"),
        link_button(
            "Twitch",
            "Directos entre semana",
            "https://twitch.tv"
        ),
        link_button(
            "Instagram",
            "Mis fotos", 
            "https://instagram.com"
        ),
        link_button(
            "Youtube",
            "Tutoriales semanales",
            "https://youtube.com"
        ),
        link_button(
            "Otro boton",
            "Mis aprendizajes y mejoras",
            "https://google.com"
        ),
        title("Segunda replica"),
        link_button(
            "Twitch",
            "Directos entre semana",
            "https://twitch.tv"
        ),
        link_button(
            "Instagram",
            "Mis fotos", 
            "https://instagram.com"
        ),
        link_button(
            "Youtube",
            "Tutoriales semanales",
            "https://youtube.com"
        ),
        link_button(
            "Otro boton",
            "Mis aprendizajes y mejoras",
            "https://google.com"
        ),
        width="100%",
    )