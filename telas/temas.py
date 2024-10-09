import flet as ft

class TemasScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

    def create_category_button(self, image_src, category_name):
        return ft.Container(
            width=150,
            height=150,
            bgcolor="transparent",
            border_radius=10,
            padding=10,
            margin=10,
            content=ft.Stack(
                controls=[
                    ft.Image(src=image_src, fit=ft.ImageFit.COVER, width=150, height=150),
                    ft.TextButton(
                        " ",  # Adicione um espaço para o botão ser clicável
                        width=150,
                        height=150,
                        on_click=lambda e: self.navigate(category_name),  # Navegação ao clicar
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.TRANSPARENT,
                            hover_bgcolor=ft.colors.TRANSPARENT,
                        )
                    )
                ]
            )
        )

    def show(self):
        self.page.title = "Categorias"

        # Banner com o título "CATEGORIAS"
        banner = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, 0),
                end=ft.Alignment(1, 0),
                colors=["#93e4ed", "#e7baff", "#93e4ed"]
            ),
            width=self.page.width,
            height=100
        )

        # Adicionando um texto para verificar se o banner aparece
        banner.content = ft.Row(
            controls=[ft.Image(src="img/BannerCateg.png")],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Criação dos botões de categoria em um layout 2x2
        grid = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.create_category_button("img/categoria_animais.png", "jogo"),
                        self.create_category_button("img/categoria_filmes.png", "jogo"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        self.create_category_button("img/categoria_acao.png", "jogo"),
                        self.create_category_button("img/categoria_desenhos.png", "jogo"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        # Layout principal da tela
        content = ft.Column(
            controls=[
                banner,
                grid,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        # Criação de um layout que ocupa toda a tela com gradiente de fundo
        main_container = ft.Container(
            content=ft.Column(
                controls=[
                    content,
                    ft.Container(expand=True),
                    self.create_nav_bar()
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=["#e5f6f8", "#f2feff"]
            ),
            height=self.page.height
        )

        # Adiciona o container principal na página
        self.page.add(main_container)
        self.page.update()

    def create_nav_bar(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.TextButton(
                        "Personalizado",
                        on_click=self.on_personalizado_click,
                        style=ft.ButtonStyle(color="black")
                    ),
                    ft.TextButton(
                        "Temas",
                        on_click=self.on_temas_click,
                        style=ft.ButtonStyle(color="black")
                    ),
                    ft.TextButton(
                        "Configuração",
                        on_click=self.on_configura_click,
                        style=ft.ButtonStyle(color="black")
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=60
            ),
            bgcolor="#93e4ed",
        )

    def on_personalizado_click(self, e):
        self.navigate("personalizado")

    def on_temas_click(self, e):
        self.navigate("temas")

    def on_configura_click(self, e):
        self.navigate("configura")
