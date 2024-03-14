import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="C.L", size="3",color_scheme="gray"),
        rx.text ("@devcat"),
        rx.text ("HOLA vsndgsjdb vbksjbksjb"),
        rx.text("""klvnnfbknornfb vjndfvojafva cjdbgvowb
                mvndlvnañsldnbñaljsv ajdvajbvñaj kjsbvajç
                nvaondva mvakjbvoa akñ vbñajb """)
    )