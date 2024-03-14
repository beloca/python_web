import reflex as rx

def link_button(text:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="alert_triangle",
                ),
                rx.vstack(
                    rx.text(text),
                    rx.text(text)
                )    
            )
        ), #así recibe aquello q pasemos en links
        href=url, #para q vaya a la de cada boton
        is_external= True, #asi cada boton abre nueva pag
        width="100%",

    )
    
