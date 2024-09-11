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
        self.page.title = "Menu"

        # Adiciona o GIF acima das imagens dos botões
        gif_image = ft.Image(src="img/logoanimada.gif", width=250, height=250)

        # Imagens personalizadas para os "botões" com GestureDetector para capturar o clique e mudar o cursor
        cadastro_button = ft.GestureDetector(
            content=ft.Image(src="img/CadastrarBt.png", width=200, height=100),
            on_tap=self.on_cadastro_click,
            mouse_cursor="click"  # Altera o cursor para "mão de seleção"
        )

        login_button = ft.GestureDetector(
            content=ft.Image(src="img/LogarBt.png", width=200, height=100),
            on_tap=self.on_login_click,
            mouse_cursor="click"  # Altera o cursor para "mão de seleção"
        )

        fechar_button = ft.GestureDetector(
            content=ft.Image(src="img/SairBt.png", width=200, height=100),
            on_tap=self.on_close_click,
            mouse_cursor="click"  # Altera o cursor para "mão de seleção"
        )

        # Cria o container de imagens (botões)
        buttons_container = ft.Column(
            controls=[
                cadastro_button,
                login_button,
                fechar_button
            ],
            alignment="center",
            spacing=20
        )

        # Cria o container principal com o GIF e os "botões" (imagens)
        menu_container = ft.Container(
            content=ft.Column(
                controls=[
                    gif_image,  # GIF na parte superior
                    buttons_container  # Imagens (botões) abaixo do GIF
                ],
                alignment="center",
                horizontal_alignment="center",  # Alinha o GIF e as imagens no centro horizontalmente
                spacing=20
            ),
            gradient=ft.RadialGradient(
                center=ft.Alignment(0.0, 0.0),  # Centraliza o gradiente
                radius=1.0,  # Ajusta o raio do gradiente
                colors=[
                    "#78d1cd",  # Cor inicial
                    "#9c96e1"   # Cor final
                ],
                stops=[0.0, 1.0]  # Paradas do gradiente
            ),
            alignment=ft.alignment.center,
            expand=True
        )

        self.page.add(menu_container)
        self.page.update()
