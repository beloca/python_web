import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

#queremos crear un span; un texto q va tomando diferentes estilos
def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.span(
            title,
            font_weight="bold",
            color="blue"
        ),
        f" {body}", 
        font_size=Size.MEDIUM.value,
        color= TextColor.BODY.value
    )