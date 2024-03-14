
import reflex as rx

from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles


class State(rx.State):
    pass #por ahora no queremos que haga nada


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                footer(),
                max_width=styles.MAX_WIDTH, #variable q hemos creado en styles
                width="100%",
                margin_y=styles.Spacer.BIG.value
                
            )
        )
    )


app = rx.App()
app.add_page(index) #para q la app añada esta pagina
app.compile()#para que compile y se ejecute