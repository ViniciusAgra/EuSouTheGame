import flet as ft
import json
import logging
from data.database import Database

class ConfiguraScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate
        self.db = Database()  # Instância do banco de dados
        self.username = self.load_current_user()  # Acessa o valor da variável de usuário
        logging.info(f"Usuário atual setado como: {self.username}")
        self.tempo_segundos = self.db.get_tempo_partida(self.username)  # Usa o valor do banco de dados ou 60

    def load_current_user(self):
        try:
            with open('user_data.json', 'r') as f:
                data = json.load(f)
                return data.get('current_user', None)  # Retorna o usuário atual ou None
        except FileNotFoundError:
            return None  # Retorna None se o arquivo não existir

    def create_container_duracao(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Image(src="img/relogiologo.png", width=50, height=50),
                    ft.Text("Duração", color="black"),
                    ft.TextField(
                        label="Seg",
                        width=100,
                        value=str(self.tempo_segundos),
                        on_change=self.on_duracao_change
                    ),
                    ft.Text("Seg", color="black")
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            bgcolor="#95e3eb",
            border_radius=10,
            padding=10,
            margin=10
        )

    def on_duracao_change(self, e):
        try:
            self.tempo_segundos = int(e.control.value)
            self.db.cursor.execute('''UPDATE users SET TempoPartida = ? WHERE username = ?''', 
                                    (self.tempo_segundos, self.username))
            self.db.conn.commit()
        except ValueError:
            pass

    def create_container_musica(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Image(src="img/musiclogo.png", width=50, height=50),
                    ft.Text("Música", color="black"),
                    ft.Switch(value=False)
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER
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
                    ft.Text("Vibrar", color="black"),
                    ft.Switch(value=False)
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            bgcolor="#95e3eb",
            border_radius=10,
            padding=10,
            margin=10
        )

    def show(self):
        self.page.title = "Configurações"

        banner = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, 0),
                end=ft.Alignment(1, 0),
                colors=["#93e4ed", "#e7baff", "#93e4ed"]
            ),
            width=self.page.width,
            height=100
        )

        banner.content = ft.Row(
            controls=[ft.Image(src="img/BannerConfig.png")],
            alignment=ft.MainAxisAlignment.CENTER
        )

        container1 = self.create_container_duracao()
        container2 = self.create_container_musica()
        container3 = self.create_container_vibrar()

        content = ft.Column(
            controls=[
                banner,
                container1,
                container2,
                container3,
                ft.Row(
                    controls=[
                        ft.GestureDetector(
                            content=ft.Image(src="img/SairBt.png", width=200, height=100),
                            on_tap=self.on_close_click,
                            mouse_cursor="click"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START
        )

        main_container = ft.Container(
            content=ft.Column(
                controls=[content, ft.Container(expand=True), self.create_nav_bar()],
                alignment=ft.MainAxisAlignment.START
            ),
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=["#e5f6f8", "#f2feff"]
            ),
            height=self.page.height
        )

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
                        style=ft.ButtonStyle(color="purple")
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                height=60
            ),
            bgcolor="#93e4ed",
        )

    def on_close_click(self, e):
        self.page.window_close()

    def on_personalizado_click(self, e):
        self.navigate("personalizado")

    def on_temas_click(self, e):
        self.navigate("temas")

    def on_configura_click(self, e):
        self.navigate("configura")
