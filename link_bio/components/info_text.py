import reflex as rx
from link_bio.styles.styles import Size as Size

#queremos crear un span; un texto q va tomando diferentes estilos
def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.chakra.span(title,font_weight="bold",color="blue"),
        f" {body}", font_size=Size.MEDIUM.value
    )