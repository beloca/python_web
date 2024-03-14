import reflex as rx
import datetime #para tener siempre actualizado el año

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"2022-{datetime.date.today().year} by DEVCAT",#este trozo lo hacemos clicable
            href="https://google.com",
            is_external=True
        ),
        rx.text("vnwejngejnnf fjebfbe"),
        padding_y="30px"
    )