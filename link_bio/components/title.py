import reflex as rx
import link_bio.styles.styles as styles

def title(text:str) -> rx.Component:
    return rx. heading( #componente para cabecera
        text,
        size="6",
        style=styles.title_style
    ) 
    