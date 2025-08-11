import flet as ft
from flet import Colors, Icons
from modelos import Usuario, Bioenergia

def main(page: ft.Page):
    page.title = "Sistema Gestión Bioenergías Tabasco"
    page.window_width = 500
    page.window_height = 700
    page.theme_mode = "light"

    mensaje_snack = ft.SnackBar(content=ft.Text(""))

    def mostrar_snack(texto):
        mensaje_snack.content.value = texto
        mensaje_snack.open = True
        page.snack_bar = mensaje_snack
        page.update()

    def limpiar_y_agregar(controles):
        page.controls.clear()
        for c in controles:
            page.controls.append(c)
        page.update()

    # --- Login ---
    usuario_input = ft.TextField(label="Usuario", width=300, icon=Icons.PERSON)
    password_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, icon=Icons.LOCK)
    btn_login = ft.ElevatedButton(
        "Ingresar",
        width=150,
        icon=Icons.KEY,
        style=ft.ButtonStyle(
            color=Colors.WHITE,
            bgcolor=Colors.PURPLE_800,
            overlay_color=Colors.PURPLE_400
        )
    )

    def validar_credenciales(e):
        u = usuario_input.value.strip()
        p = password_input.value.strip()
        if u == "demo" and p == "demo":
            mostrar_snack("Login correcto")
            mostrar_menu()
        else:
            mostrar_snack("Usuario o contraseña incorrectos")

    btn_login.on_click = validar_credenciales

    def mostrar_login():
        controles = [
            ft.Row(
                [ft.Icon(Icons.KEY, size=80, color=Colors.PURPLE_800)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text("Iniciar sesión", size=30, weight=ft.FontWeight.BOLD, color=Colors.PURPLE_900, text_align=ft.TextAlign.CENTER),
            usuario_input,
            password_input,
            btn_login,
        ]
        limpiar_y_agregar([
            ft.Column(controles,
                      alignment=ft.MainAxisAlignment.CENTER,
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                      spacing=20,
                      expand=True)
        ])

    # --- menú principal con botones estilo cuadro y animación ---
    def mostrar_menu():
        def cuadro_boton(texto, icono, color_bg, on_click):
            container = ft.Container(
                width=300,
                height=80,
                bgcolor=color_bg,
                border_radius=10,
                alignment=ft.alignment.center,
                content=ft.Row(
                    [
                        ft.Icon(icono, size=30, color=Colors.WHITE),
                        ft.Text(texto, size=20, weight=ft.FontWeight.BOLD, color=Colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=15,
                ),
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=0,
                    color=Colors.TRANSPARENT,
                    offset=ft.Offset(0, 0),
                ),
            )

            def on_hover(e: ft.HoverEvent):
                if e.data == "true":
                    container.shadow = ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=Colors.PURPLE_300,
                        offset=ft.Offset(0, 4),
                    )
                    container.update()
                else:
                    container.shadow = ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=0,
                        color=Colors.TRANSPARENT,
                        offset=ft.Offset(0, 0),
                    )
                    container.update()

            container.on_hover = on_hover
            container.on_click = on_click
            return container

        controles = [
            ft.Text(
                "Menú principal",
                size=40,
                weight=ft.FontWeight.BOLD,
                color=Colors.PURPLE_900,
                text_align=ft.TextAlign.CENTER,
                style=ft.TextThemeStyle.HEADLINE_MEDIUM,
            ),
            ft.Container(height=30),
            cuadro_boton(
                "Agregar nuevo usuario",
                Icons.PERSON_ADD,
                Colors.PURPLE_900,
                on_click=lambda e: mostrar_agregar_usuario()
            ),
            cuadro_boton(
                "Consultar usuarios",
                Icons.PEOPLE,
                Colors.PURPLE_700,
                on_click=lambda e: mostrar_consultar_usuarios()
            ),
            cuadro_boton(
                "Agregar bioenergía",
                Icons.ENERGY_SAVINGS_LEAF,
                Colors.PURPLE_600,
                on_click=lambda e: mostrar_agregar_bioenergia()
            ),
            cuadro_boton(
                "Consultar bioenergías",
                Icons.SPA,
                Colors.PURPLE_600,
                on_click=lambda e: mostrar_consultar_bioenergia()
            ),
            cuadro_boton(
                "Cerrar sesión",
                Icons.LOGOUT,
                Colors.PURPLE_900,
                on_click=lambda e: mostrar_login()
            ),
        ]

        limpiar_y_agregar([
            ft.Column(
                controles,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                expand=True
            )
        ])

    # --- AGREGAR USUARIO ---
    nombre_input = ft.TextField(label="Nombre", width=300, icon=Icons.BADGE)
    clave_input = ft.TextField(label="Usuario (clave)", width=300, icon=Icons.PERSON)
    contra_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, icon=Icons.LOCK)
    btn_registrar_usuario = ft.ElevatedButton(
        "Registrar usuario",
        width=150,
        icon=Icons.CHECK,
        style=ft.ButtonStyle(bgcolor=Colors.PURPLE_700, color=Colors.WHITE)
    )

    def registrar_usuario(e):
        n = nombre_input.value.strip()
        c = clave_input.value.strip()
        p = contra_input.value.strip()
        if not n or not c or not p:
            mostrar_snack("Todos los campos son obligatorios")
            return
        try:
            nuevo = Usuario(nombre=n, clave=c, contra=p, admin=False)
            nuevo.save()
            mostrar_snack("Usuario registrado correctamente")
            nombre_input.value = clave_input.value = contra_input.value = ""
            page.update()
        except Exception as err:
            mostrar_snack("Error al registrar usuario en Airtable")
            print("Error registrar usuario:", err)

    btn_registrar_usuario.on_click = registrar_usuario

    def mostrar_agregar_usuario():
        controles = [
            ft.Text("Agregar nuevo usuario", size=30, weight=ft.FontWeight.BOLD, color=Colors.PURPLE_700, text_align=ft.TextAlign.CENTER),
            nombre_input,
            clave_input,
            contra_input,
            btn_registrar_usuario,
            ft.ElevatedButton("Volver al menú", width=150, on_click=lambda e: mostrar_menu()),
        ]
        limpiar_y_agregar([
            ft.Column(controles,
                      spacing=15,
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                      alignment=ft.MainAxisAlignment.CENTER,
                      expand=True)
        ])

    # --- CONSULTAR USUARIOS ---
    def mostrar_consultar_usuarios():
        try:
            registros = Usuario.all()
            filas = []
            for r in registros:
                filas.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(r.nombre)),
                            ft.DataCell(ft.Text(r.clave)),
                            ft.DataCell(ft.Text(r.contra)),
                            ft.DataCell(ft.Text("Sí" if r.admin else "No")),
                        ]
                    )
                )
            tabla = ft.DataTable(
                columns=[
                    ft.DataColumn(label=ft.Text("Nombre")),
                    ft.DataColumn(label=ft.Text("Usuario")),
                    ft.DataColumn(label=ft.Text("Contraseña")),
                    ft.DataColumn(label=ft.Text("Admin")),
                ],
                rows=filas,
                heading_row_color=Colors.AMBER_100,
                border=ft.border.all(1, Colors.BLACK),
                width=880,
            )
            controles = [
                ft.Text("Usuarios registrados", size=30, weight=ft.FontWeight.BOLD, color=Colors.PURPLE_700, text_align=ft.TextAlign.CENTER),
                ft.ListView(
                    [tabla],
                    width=900,
                    height=350,
                    padding=10,
                ),
                ft.ElevatedButton("Volver al menú", width=150, on_click=lambda e: mostrar_menu()),
            ]
            limpiar_y_agregar([
                ft.Column(controles,
                          spacing=15,
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          alignment=ft.MainAxisAlignment.CENTER,
                          expand=True)
            ])
        except Exception as err:
            mostrar_snack("Error al obtener usuarios de Airtable")
            print("Error consultar usuarios:", err)

    # --- AGREGAR BIOENERGÍA ---
    cultivo_input = ft.TextField(label="Cultivo", width=300, icon=Icons.GRASS)
    parte_input = ft.TextField(label="Parte", width=300, icon=Icons.PARTY_MODE)
    cantidad_input = ft.TextField(label="Cantidad", width=300, keyboard_type=ft.KeyboardType.NUMBER, icon=Icons.FORMAT_LIST_NUMBERED)
    area_input = ft.TextField(label="Área", width=300, keyboard_type=ft.KeyboardType.NUMBER, icon=Icons.SQUARE_FOOT)
    energia_input = ft.TextField(label="Energía", width=300, keyboard_type=ft.KeyboardType.NUMBER, icon=Icons.BOLT)
    municipio_input = ft.TextField(label="Municipio", width=300, icon=Icons.LOCATION_CITY)
    latitud_input = ft.TextField(label="Latitud", width=300, keyboard_type=ft.KeyboardType.NUMBER, icon=Icons.PIN)
    longitud_input = ft.TextField(label="Longitud", width=300, keyboard_type=ft.KeyboardType.NUMBER, icon=Icons.PIN)
    btn_registrar_bioenergia = ft.ElevatedButton(
        "Registrar bioenergía",
        width=150,
        icon=Icons.CHECK,
        style=ft.ButtonStyle(bgcolor=Colors.PURPLE_700, color=Colors.WHITE)
    )

    def registrar_bioenergia(e):
        try:
            cultivo = cultivo_input.value.strip()
            parte = parte_input.value.strip()
            municipio = municipio_input.value.strip()

            if not cultivo or not parte or not municipio:
                mostrar_snack("Los campos cultivo, parte y municipio son obligatorios")
                return

            def parse_float(valor, nombre):
                if not valor.strip():
                    raise ValueError(f"El campo {nombre} es obligatorio")
                return float(valor.replace(",", "."))

            cantidad = parse_float(cantidad_input.value, "cantidad")
            area = parse_float(area_input.value, "área")
            energia = parse_float(energia_input.value, "energía")
            latitud = parse_float(latitud_input.value, "latitud")
            longitud = parse_float(longitud_input.value, "longitud")

            nueva = Bioenergia(
                cultivo=cultivo,
                parte=parte,
                cantidad=cantidad,
                area=area,
                energia=energia,
                municipio=municipio,
                latitud=latitud,
                longitud=longitud,
            )
            nueva.save()
            mostrar_snack("Bioenergía registrada correctamente")

            cultivo_input.value = parte_input.value = municipio_input.value = ""
            cantidad_input.value = area_input.value = energia_input.value = ""
            latitud_input.value = longitud_input.value = ""
            page.update()

        except ValueError as ve:
            mostrar_snack(str(ve))
        except Exception as err:
            mostrar_snack("Error al registrar bioenergía")
            print("Error registrar bioenergía:", err)

    btn_registrar_bioenergia.on_click = registrar_bioenergia

    def mostrar_agregar_bioenergia():
        controles = [
            ft.Text("Agregar bioenergía", size=30, weight=ft.FontWeight.BOLD, color=Colors.PURPLE_700, text_align=ft.TextAlign.CENTER),
            cultivo_input,
            parte_input,
            cantidad_input,
            area_input,
            energia_input,
            municipio_input,
            latitud_input,
            longitud_input,
            btn_registrar_bioenergia,
            ft.ElevatedButton("Volver al menú", width=150, on_click=lambda e: mostrar_menu()),
        ]
        limpiar_y_agregar([
            ft.Column(controles,
                      spacing=15,
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                      alignment=ft.MainAxisAlignment.CENTER,
                      expand=True)
        ])

    # --- CONSULTAR BIOENERGÍAS ---
    def mostrar_consultar_bioenergia():
        try:
            registros = Bioenergia.all()
            filas = []
            for r in registros:
                filas.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(r.cultivo)),
                            ft.DataCell(ft.Text(r.parte)),
                            ft.DataCell(ft.Text(str(r.cantidad))),
                            ft.DataCell(ft.Text(str(r.area))),
                            ft.DataCell(ft.Text(str(r.energia))),
                            ft.DataCell(ft.Text(r.municipio)),
                            ft.DataCell(ft.Text(str(r.latitud))),
                            ft.DataCell(ft.Text(str(r.longitud))),
                        ]
                    )
                )
            tabla = ft.DataTable(
                columns=[
                    ft.DataColumn(label=ft.Text("Cultivo")),
                    ft.DataColumn(label=ft.Text("Parte")),
                    ft.DataColumn(label=ft.Text("Cantidad")),
                    ft.DataColumn(label=ft.Text("Área")),
                    ft.DataColumn(label=ft.Text("Energía")),
                    ft.DataColumn(label=ft.Text("Municipio")),
                    ft.DataColumn(label=ft.Text("Latitud")),
                    ft.DataColumn(label=ft.Text("Longitud")),
                ],
                rows=filas,
                heading_row_color=Colors.AMBER_100,
                border=ft.border.all(1, Colors.BLACK),
                width=880,
            )
            controles = [
                ft.Text("Bioenergías registradas", size=30, weight=ft.FontWeight.BOLD, color=Colors.PURPLE_700, text_align=ft.TextAlign.CENTER),
                ft.ListView(
                    [tabla],
                    width=900,
                    height=350,
                    padding=10,
                ),
                ft.ElevatedButton("Volver al menú", width=150, on_click=lambda e: mostrar_menu()),
            ]
            limpiar_y_agregar([
                ft.Column(controles,
                          spacing=15,
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          alignment=ft.MainAxisAlignment.CENTER,
                          expand=True)
            ])
        except Exception as err:
            mostrar_snack("Error al obtener bioenergías")
            print("Error consultar bioenergías:", err)

    mostrar_login()

if __name__ == "__main__":
    ft.app(target=main)
