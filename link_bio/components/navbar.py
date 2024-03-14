import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "DevCat",
            height="40px",
            padding_x="30px"
        ),
        position="sticky", #para q esta parte superior quede fija
        bg="blue",
        padding_y="8px",
        z_index="999" #asegurarnos q siempre este en la parte superior 
    )