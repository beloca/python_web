import reflex as rx

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
                align_items="start"
            )
        ),
        rx.text("""klvnnfbknornfb vjndfvojafva cjdbgvowb
                mvndlvnañsldnbñaljsv ajdvajbvñaj kjsbvajç
                nvaondva mvakjbvoa akñ vbñajb """),
        align_items="start"   
    )