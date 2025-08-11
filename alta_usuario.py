import flet as ft 

def main(page: ft.Page):
    # Configuración de la página 
    page.title = "Altas"
    page.theme_mode = "light"
    page.window.width = 800
    page.window.height = 600
    page.padding = 30  # Margen interno
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "grey100"

    page.appbar = ft.AppBar(
        title=ft.Text("Nuevo usuario", style=ft.TextStyle(weight="bold", size=20)),
        leading=ft.Icon("person_add"),
        color="white",
        bgcolor="deepPurple"
    )

    # Componentes de la página
    txt_clave = ft.TextField(label="Clave del usuario", width=400)
    txt_contra = ft.TextField(label="Contraseña", password=True, width=400, can_reveal_password=True)
    txt_contra2 = ft.TextField(label="Confirmar contraseña", password=True, width=400, can_reveal_password=True)
    txt_nombre = ft.TextField(label="Nombre completo", width=400)
    chk_admin = ft.Checkbox(label="¿Es administrador?")
    
    btn_guardar = ft.FilledButton(
        text="Guardar",
        icon=ft.Icon("save"),
        style=ft.ButtonStyle(bgcolor="deepPurple", color="white")
    )

    btn_cancelar = ft.FilledButton(
        text="Cancelar",
        icon=ft.Icon("cancel"),
        style=ft.ButtonStyle(bgcolor="red400", color="white")
    )

    fila = ft.Row(
        controls=[btn_guardar, btn_cancelar],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        spacing=20
    )

    # Contenedor con tarjeta para agrupar el formulario
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    txt_clave,
                    txt_contra,
                    txt_contra2,
                    txt_nombre,
                    chk_admin,
                    fila
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START
            ),
            padding=30,
            width=500,
            bgcolor="white",
            border_radius=10,
            shadow=ft.BoxShadow(blur_radius=12, color="grey400", spread_radius=1)
        )
    )

    # Añadir componentes a la página 
    page.add(card)
    page.update()

ft.app(target=main)

