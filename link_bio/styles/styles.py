import reflex as rx
from enum import Enum #biblio de python
from .colors import Color as Color
from .colors import TextColor as TextColor
#constants
MAX_WIDTH="600px"


#Sizes
class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"

#estilo para q todos los botones se comporten =
BASE_STYLE={ #se añade en index, en rx.App para q coja este estilo
    "background_color": Color.BACKGROUND.value,
    rx.button:{
        "width":"100%", #es un mapa por eso :
        "height":"100%",
        "display":"block", #alineado a la izq
        "padding":Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color":Color.CONTENT.value,
        "_hover":{
            "background_color":Color.SECONDARY.value
        }
    },
    rx.link:{ #para q link no se subraye al poner el raton
        "text_decoration": "none",
        "_hover":{} #para q no tenga nada
    }
}

title_style=dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)
button_title_style= dict ( #se define asi porq no es componente q exista,sino estilo propio
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)
button_body_style=dict( #lo añadimos en link_button llamando a esta variable
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)



