import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="C.L", size="3",color_scheme="gray"),
            rx.vstack(
                rx.heading (
                    "Cata Lobo",
                    size="6"
                ),
                rx.text (
                    "@devcat",
                    margin_top="-10px" #para q no nos deje margen superior y lo pegue al texto de arriba
                ),
                rx.hstack(
                    link_icon("https://instagram.com/beloca_4"), #traemos el icono creado y hacemos hstack para horizontal
                    link_icon("https://instagram.com/beloca_4"),
                ),
                align_items="start",
            ),
            spacing=="5"
        ),
        rx.flex( #separar elementos dentros de la misma forma. un layout
            info_text("+1", "año experiencia"),
            rx.spacer(),
            info_text("+1", "año experiencia"),
            rx.spacer(),
            info_text("+1", "año experiencia"),
            width="100%" #si ponemos sapcer pero no decimos q ocupe el 100% no hará nada
        ),

        rx.text("""klvnnfbknornfb vjndfvojafva cjdbgvowb
                mvndlvnañsldnbñaljsv ajdvajbvñaj kjsbvajç
                nvaondva mvakjbvoa akñ vbñajb """),
        spacing="5", #espacio que dejamos entre cada uno de los componentes
        align_items="start"   
    )