import reflex as rx
import link_bio.styles.styles as styles
def link_button(title:str,body:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="moon",
                    width=styles.Size.DEFAULT.value,
                    height=styles.Size.BIG.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start"
                )    
            )
        ), #así recibe aquello q pasemos en links
        href=url, #para q vaya a la de cada boton
        is_external= True, #asi cada boton abre nueva pag
        width="100%",

    )
    
