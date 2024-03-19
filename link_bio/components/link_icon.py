import reflex as rx
import link_bio.styles.styles as styles


def link_icon(url:str) -> rx.Component: #queremos hacer icono clickable
    return rx.link(
        rx.icon(
            tag="instagram",
        ),
        href=url,
        is_external=True
    )