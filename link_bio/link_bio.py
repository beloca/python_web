
import reflex as rx

from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer

class State(rx.State):
    pass #por ahora no queremos que haga nada


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
    )

app = rx.App()
app.add_page(index) #para q la app añada esta pagina
app.compile()#para que compile y se ejecute