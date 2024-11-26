import flet as ft

class RankScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

    def create_container_duracao(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Image(src="img/relogiologo.png", width=50, height=50),
                    ft.Text("Duração", color="black"),  # Texto preto
                    ft.TextField(
                        label="Seg",
                        width=100
                    ),
                    ft.Text("Seg", color="black")  # Texto preto
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER  # Centraliza o conteúdo
            ),
            bgcolor="#95e3eb",
            border_radius=10,
            padding=10,
            margin=10
        )

    def create_container_musica(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Image(src="img/musiclogo.png", width=50, height=50),
                    ft.Text("Música", color="black"),  # Texto preto
                    ft.Switch(value=False)
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER  # Centraliza o conteúdo
            ),
            bgcolor="#95e3eb",
            border_radius=10,
            padding=10,
            margin=10
        )

    def create_container_vibrar(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Image(src="img/vibrarlogo.png", width=50, height=50),
                    ft.Text("Vibrar", color="black"),  # Texto preto
                    ft.Switch(value=False)
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER  # Centraliza o conteúdo
            ),
            bgcolor="#95e3eb",
            border_radius=10,
            padding=10,
            margin=10
        )

    def show(self):
        self.page.title = "Temas"

        # Criação de um container com gradiente linear ocupando toda a largura
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
            controls=[ft.Image(src="img/BannerConfig.png")],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Criação dos containers individuais
        container1 = self.create_container_duracao()
        container2 = self.create_container_musica()
        container3 = self.create_container_vibrar()

        # Criação de um layout de coluna que alinha o banner e os containers
        content = ft.Column(
            controls=[
                banner,  # Adiciona o banner com gradiente aqui
                container1,
                container2,
                container3,
                ft.Row(  # Colocando o botão em um Row para centralizar
                    controls=[
                        ft.GestureDetector(
                            content=ft.Image(src="img/SairBt.png", width=200, height=100),
                            on_tap=self.on_close_click,
                            mouse_cursor="click"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER  # Centraliza o botão
                )
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,  # Garante que o conteúdo comece do topo
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
                        "Rank",
                        on_click=self.on_rank_click,
                        style=ft.ButtonStyle(color="purple")
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

    def on_close_click(self, e):
        self.page.window_close()
        
    # Métodos para navegar entre telas
    def on_rank_click(self, e):
        self.navigate("rank")  # Substitua pelo método de navegação correto

    def on_temas_click(self, e):
        self.navigate("temas")  # Substitua pelo método de navegação correto

    def on_configura_click(self, e):
        self.navigate("configura")  # Substitua pelo método de navegação correto
