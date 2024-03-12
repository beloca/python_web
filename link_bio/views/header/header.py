import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Cata Lobo", size="7"),
        rx.text ("@devcat"),
        rx.text ("HOLA vsndgsjdb vbksjbksjb"),
        rx.text("""klvnnfbknornfb vjndfvojafva cjdbgvowb
                mvndlvnañsldnbñaljsv ajdvajbvñaj kjsbvajç
                nvaondva mvakjbvoa akñ vbñajb """)
    )