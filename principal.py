import flet as ft
from pyairtable import Api
from pyairtable.formulas import match

# Airtable config
API_KEY = "patCJHPsDL7m21JV7.bf57d0d57c46b04f0389db4579826244822df412291c5bf64b721e4614abdd55"
BASE_ID = "appktXM30kKg7swqX"
TABLE_NAME = "Usuario"

api = Api(API_KEY)
tabla_usuarios = api.base(BASE_ID).table(TABLE_NAME)

def main(page: ft.Page):
    page.title = "Sistema de Gestión"
    page.theme_mode = "light"

    # ---------------- Login ----------------
    usuario_input = ft.TextField(label="Usuario")
    password_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    mensaje_snack = ft.SnackBar(content=ft.Text(""))

    def mostrar_snack(texto):
        mensaje_snack.content.value = texto
        mensaje_snack.open = True
        page.snack_bar = mensaje_snack
        page.update()

    def validar_credenciales(e):
        usuario = usuario_input.value
        password = password_input.value

        try:
            formula = match({"clave": usuario, "contra": password})
            registro = tabla_usuarios.first(formula=formula)
            if registro:
                print("Funciona!")
                page.go("/menu")
            else:
                print(f"Usuario '{usuario}' no encontrado.")
                mostrar_snack("Usuario o contraseña incorrectos.")
        except Exception as err:
            print(f"Error de Airtable: {err}")
            mostrar_snack("Error de conexión con Airtable.")

    # ---------------- Menú principal ----------------
    def mostrar_menu_principal():
        page.views.append(
            ft.View(
                route="/menu",
                controls=[
                    ft.AppBar(
                        title=ft.Text("SISTEMA DE GESTIÓN DE USUARIOS"),
                        leading=ft.Icon("people"),
                        bgcolor="purple",
                        color="white"
                    ),
                    ft.Column(
                        controls=[
                            ft.ElevatedButton("Agregar nuevo usuario", on_click=lambda e: page.go("/agregar_usuario")),
                            ft.ElevatedButton("Consultar usuarios", on_click=lambda e: page.go("/consultar_usuarios")),
                            ft.ElevatedButton("Cerrar sesión", on_click=lambda e: page.go("/"))
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.update()

    # ---------------- Agregar usuario ----------------
    def mostrar_agregar_usuario():
        nombre = ft.TextField(label="Nombre")
        clave = ft.TextField(label="Usuario (clave)")
        contra = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)

        def registrar_usuario(e):
            if not nombre.value or not clave.value or not contra.value:
                mostrar_snack("Todos los campos son obligatorios.")
                return
            try:
                tabla_usuarios.create({
                    "nombre": nombre.value,
                    "clave": clave.value,
                    "contra": contra.value
                })
                mostrar_snack("Usuario registrado correctamente.")
                nombre.value = clave.value = contra.value = ""
                page.update()
            except Exception as err:
                print("Error al registrar:", err)
                mostrar_snack("Error al registrar en Airtable.")

        page.views.append(
            ft.View(
                route="/agregar_usuario",
                controls=[
                    ft.AppBar(title=ft.Text("Agregar nuevo usuario")),
                    nombre,
                    clave,
                    contra,
                    ft.ElevatedButton("Registrar", on_click=registrar_usuario),
                    ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/menu"))
                ]
            )
        )
        page.update()

    # ---------------- Consultar usuarios ----------------
    def mostrar_consultar_usuarios():
        try:
            registros = tabla_usuarios.all()
            filas = []

            for r in registros:
                data = r["fields"]
                filas.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(data.get("nombre", ""))),
                            ft.DataCell(ft.Text(data.get("clave", ""))),
                            ft.DataCell(ft.Text(data.get("contra", "")))
                        ]
                    )
                )

            tabla = ft.DataTable(
                columns=[
                    ft.DataColumn(label=ft.Text("Nombre")),
                    ft.DataColumn(label=ft.Text("Usuario")),
                    ft.DataColumn(label=ft.Text("Contraseña"))
                ],
                rows=filas
            )

            page.views.append(
                ft.View(
                    route="/consultar_usuarios",
                    controls=[
                        ft.AppBar(title=ft.Text("Usuarios registrados")),
                        tabla,
                        ft.ElevatedButton("Volver al menú", on_click=lambda e: page.go("/menu"))
                    ]
                )
            )
        except Exception as err:
            print("Error al consultar:", err)
            mostrar_snack("Error al obtener datos de Airtable.")
        page.update()

    # ---------------- Rutas ----------------
    def cambiar_ruta(route):
        if page.route == "/":
            page.views.clear()
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.AppBar(title=ft.Text("Iniciar sesión")),
                        usuario_input,
                        password_input,
                        ft.ElevatedButton("Ingresar", on_click=validar_credenciales)
                    ]
                )
            )
        elif page.route == "/menu":
            mostrar_menu_principal()
        elif page.route == "/agregar_usuario":
            mostrar_agregar_usuario()
        elif page.route == "/consultar_usuarios":
            mostrar_consultar_usuarios()

        page.update()

    page.on_route_change = cambiar_ruta
    page.go(page.route)

ft.app(target=main)

