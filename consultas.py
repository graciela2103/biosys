import flet as ft
from simpledt import SQLDataTable

def main(page:ft.Page):
    page.title="consultas"
    page.theme_mode="light"
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    page.appbar=ft.AppBar(
        title=ft.Text("listado de usuario"),
        center_title=True,
        leading=ft.Icon("people"),
        bgcolor="blue",
        color="white"
    )
    base_datos = SQLDataTable("sqlite", "base_datos.db", "usuario")
    tbl_usuarios = base_datos.datatable


    page.add(tbl_usuarios)
    page.update()


ft.app(target=main)