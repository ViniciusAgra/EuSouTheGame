import flet as ft

class TemasScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

    def create_container_duracao(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Image(src="img/relogiologo.png", width=50, height=50),
                    ft.Text("Duração"),
                    ft.TextField(
                        label="Seg",
                        width=100
                    ),
                    ft.Text("Seg")
                ],
                spacing=10
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
                    ft.Text("Música"),
                    ft.Switch(value=False)
                ],
                spacing=10
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
                    ft.Text("Vibrar"),
                    ft.Switch(value=False)
                ],
                spacing=10
            ),
            bgcolor="#95e3eb",
            border_radius=10,
            padding=10,
            margin=10
        )

    def show(self):
        self.page.title = "Temas"
        banner = ft.Image(src="img/BannerConfig.png", width=self.page.width, height=100)

        # Criação dos containers individuais
        container1 = self.create_container_duracao()
        container2 = self.create_container_musica()
        container3 = self.create_container_vibrar()

        # Criação de um layout de coluna que alinha o banner e os containers
        content = ft.Column(
            controls=[
                ft.Container(
                    content=banner,
                    width=self.page.width,
                    padding=0,
                    margin=0
                ),
                container1,
                container2,
                container3,
                ft.GestureDetector(
                    content=ft.Image(src="img/SairBt.png", width=200, height=100),
                    on_tap=self.on_close_click,
                    mouse_cursor="click"
                )
            ],
            spacing=20
        )

        self.page.add(content)
        self.page.update()

    def on_close_click(self, e):
        self.page.window_close()
