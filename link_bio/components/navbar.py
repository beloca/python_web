import reflex as rx
from link_bio.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "DevCat"
        ),
        position="sticky", #para q esta parte superior quede fija
        bg="lightgray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999", #asegurarnos q siempre este en la parte superior 
        top="0" #indica que es cero a la parte superior, por eso bajas barra pero no se mueve la navbar
    )