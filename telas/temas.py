import flet as ft
import json

class TemasScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

    def create_category_button(self, image_src, tag):
        return ft.TextButton(
            content=ft.Container(
                width=150,
                height=150,
                bgcolor="transparent",  # Fundo transparente para ver a imagem de fundo
                border_radius=10,
                padding=10,
                margin=10,
                # Utilizando a imagem como fundo
                content=ft.Stack(
                    controls=[
                        ft.Image(src=image_src, fit=ft.ImageFit.COVER, width=150, height=150),
                    ]
                )
            ),
            on_click=self.on_category_button_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                overlay_color="transparent"  # Remove a cor de fundo ao passar o mouse
            )
        )

    def on_category_button_click(self,e):
        print(dir(e.control))
        self.navigate("jogo")
        with open('data/user_data.json', 'w') as f:
            json.dump({'temaatual':"" }, f)

    def show(self):
        self.page.title = "Categorias"

        # Banner com o título "CATEGORIAS"
        banner = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, 0),  # Começo do gradiente (esquerda)
                end=ft.Alignment(1, 0),      # Fim do gradiente (direita)
                colors=["#93e4ed", "#e7baff", "#93e4ed"]
            ),
            width=self.page.width,  # Define a largura como a largura da tela
            height=100  # Altura do banner
        )

        # Adicionando um texto para verificar se o banner aparece
        banner.content = ft.Row(
            controls=[ft.Image(src="img/BannerCateg.png")],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Criação dos botões
        grid = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.create_category_button("img/categoria_animais.png","animais"),
                        self.create_category_button("img/categoria_filmes.png","filme"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        self.create_category_button("img/categoria_acao.png","ação"),
                        self.create_category_button("img/categoria_desenhos.png","desenho"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza as linhas
        )

        # Layout principal da tela
        content = ft.Column(
            controls=[
                banner,
                grid,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,  # Garante que o conteúdo comece do topo
        )

        # Criação de um layout que ocupa toda a tela com gradiente de fundo
        main_container = ft.Container(
            content=ft.Column(
                controls=[
                    content,
                    ft.Container(expand=True),  # Container vazio para ocupar o restante do espaço
                    self.create_nav_bar()  # Colocando a navbar aqui
                ],
                alignment=ft.MainAxisAlignment.START,  # Garante que tudo comece do topo
            ),
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, -1),  # Começa no topo
                end=ft.Alignment(0, 1),     # Vai até o final da tela
                colors=["#e5f6f8", "#f2feff"]  # Gradiente de 180° com as cores especificadas
            ),
            height=self.page.height  # Força a altura do container principal
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
