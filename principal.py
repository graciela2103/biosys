import flet as ft

def main(page:ft.Page):
    page.title= "menu principal"
    page.theme_mode= "light"
    page.appbar=ft.AppBar(
        title=ft.Text ("SISTEMA DE GESTION DE ENERGIAS"),
        leading=ft.Icon("energy_sevings_leaf"),
        color="white",
        bgcolor="purple"
    )

    btn_registro=ft.ElevatedButton("Registro")
    btn_consulta=ft.ElevatedButton("Consulta")

    page.add(btn_registro,btn_consulta)
    page.update()

ft.app(target=main)