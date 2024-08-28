import flet as ft
import time

class SplashScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

    def show(self):
        splash_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src="img\logoanimada.gif", width=200, height=200),
                ],
                alignment="center",
                spacing=20
            ),
            bgcolor="#6a0dad",  # Fundo roxo
            alignment=ft.alignment.center,
            expand=True
        )
        
        self.page.add(splash_container)
        self.page.update()  # Força uma atualização da interface

        # Aguarda por 10 segundos antes de navegar para a próxima tela
        time.sleep(5)

        # Após o delay, navega para a tela de navegação
        self.navigate("navegacao")  # Chama a função de navegação