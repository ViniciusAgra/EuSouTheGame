import flet as ft
#from telas.configura import ConfiguraScreen
# from telas.personalizado import PersonalizadoScreen
from telas.temas import TemasScreen

class PrincipalScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

    def on_configura_click(self, e):
        self.show_configura()

    def on_personalizado_click(self, e):
        self.show_personalizado()

    def on_temas_click(self, e):
        self.show_temas()

    # def show_configura(self):
    #     ConfiguraScreen(self.page, self.navigate).show()

    # def show_personalizado(self):
    #     PersonalizadoScreen(self.page, self.navigate).show()

    def show_temas(self):
        TemasScreen(self.page, self.navigate).show()

    def show(self):
        # Define qual tela será exibida inicialmente
        self.show_temas()  # Inicialmente exibe a tela de Temas

        # Cria a barra de navegação
        nav_bar = ft.Row(
            controls=[
                ft.TextButton("Configura", on_click=self.on_configura_click),
                ft.TextButton("Personalizado", on_click=self.on_personalizado_click),
                ft.TextButton("Temas", on_click=self.on_temas_click),
            ],
            alignment="center",
            spacing=20,
            padding=10,
        )

        # Layout da tela principal
        principal_layout = ft.Column(
            controls=[
                # Espaço para o conteúdo principal, que será definido pela função show_temas ou outras
                nav_bar,
            ],
            alignment="center",
            spacing=10,
        )

        self.page.add(principal_layout)
        self.page.update()
