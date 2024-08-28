import flet as ft

class MenuScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

    def on_cadastro_click(self, e):
        self.navigate("cadastro")

    def on_login_click(self, e):
        self.navigate("login")

    def on_close_click(self, e):
        self.page.window_close()

    def show(self):
        self.page.title = "Navegação"

        menu_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton("Cadastrar", on_click=self.on_cadastro_click),
                    ft.ElevatedButton("Logar", on_click=self.on_login_click),
                    ft.ElevatedButton("Fechar", on_click=self.on_close_click)
                ],
                alignment="center",
                spacing=20
            ),
            bgcolor="#9c27b0",  # Fundo roxo claro
            alignment=ft.alignment.center,
            expand=True
        )

        self.page.add(menu_container)
        self.page.update()
