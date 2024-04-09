
import reflex as rx

from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size #asi no hay que acceder a traves de styles sino direcctamente



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
                margin_y=Size.BIG.value ,
                             
            ),
            bg="darkgrey"
        )
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index) #para q la app añada esta pagina
app.compile()#para que compile y se ejecute