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
                    ft.Image(src="img/logoanimada.gif", width=200, height=200),
                ],
                alignment="center",
                spacing=20
            ),
            gradient=ft.RadialGradient(
                center=ft.Alignment(0.0, 0.0),  # Centraliza o gradiente
                radius=1.0,  # Ajusta o raio do gradiente
                colors=[
                    "#b2f3f6",  # Cor inicial
                    "#9c96e1"   # Cor final
                ],
                stops=[0.0, 1.0]  # Paradas do gradiente
            ),
            alignment=ft.alignment.center,
            expand=True
        )
        
        self.page.add(splash_container)
        self.page.update()  # Força uma atualização da interface

        # Aguarda por 5 segundos antes de navegar para a próxima tela
        time.sleep(3)

        # Após o delay, navega para a tela de navegação
        self.navigate("menu")  # Chama a função de navegação
