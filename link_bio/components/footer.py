import reflex as rx
import datetime #para tener siempre actualizado el año
from link_bio.styles.styles import Size as Size
def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            f"@ 2022-{datetime.date.today().year} by DEVCAT",#este trozo lo hacemos clicable
            href="https://google.com",
            is_external=True,
            font_size=Size.MEDIUM.value,
            margin="-10px"
        ),
        rx.text(
            "vnwejngejnnf fjebfbe eibeub  jnvsbs bvw",
            font_size=Size.MEDIUM.value,
        ),
        rx.image(src="logo_ojo2.png", height="150px"),
        margin_bottom=Size.BIG.value,
        padding_y="30px",
        align="center"
    )