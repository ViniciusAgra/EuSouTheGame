import flet as ft
import logging
from database import Database

logging.basicConfig(
    filename='app.log', 
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger()

# Variável global para armazenar o nome do usuário
current_user = None

class LoginScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate
        self.db = Database()  # Inicializa o banco de dados

    def on_login_click(self, e):
        username = self.username_field.value
        password = self.password_field.value

        logging.info(f"Botão de login clicado. Usuário: '{username}'")

        if self.verify_login(username, password):
            global current_user  # Use a variável global
            current_user = username  # Armazena o nome do usuário logado
            logging.info(f"Usuario '{username}' fez login com sucesso.")
            logging.info(f"Usuario atual setado como: {current_user}")  # Mensagem de log
            self.navigate("temas")
        else:
            logging.warning(f"Tentativa de login falhou para o usuário '{username}'.")
            self.page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha incorretos"), bgcolor="#ff0000", open=True)
            self.page.update()

    def on_menu_click(self, e):
        self.navigate("menu")

    def verify_login(self, username, password):
        user = self.db.get_user_by_username(username)
        if user and user[2] == password:
            logging.info(f"Usuario '{username}' encontrado e senha corresponde.")
            return True
        else:
            logging.info(f"Usuario '{username}' não encontrado ou senha incorreta.")
            return False

    def show(self):
        self.page.title = "Login"

        self.username_field = ft.TextField(
            label="Usuário", 
            hint_text="Digite seu usuário", 
            width=300, 
            bgcolor="#8c68ca",
            border_color="#aeeef0",
            border_width=2,
            color="#aeeef0"  # Cor do texto inserido
        )
        self.password_field = ft.TextField(
            label="Senha", 
            hint_text="Digite sua senha", 
            password=True, 
            width=300, 
            bgcolor="#8c68ca",
            border_color="#aeeef0",
            border_width=2,
            color="#aeeef0"  # Cor do texto inserido
        )

        login_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src="img/logoanimada.gif", width=300, height=300),
                    self.username_field,
                    self.password_field,
                    ft.ElevatedButton("Login", on_click=self.on_login_click),
                    ft.TextButton("Voltar Ao Menu", on_click=self.on_menu_click, style=ft.ButtonStyle(color=ft.colors.BLACK))
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=20
            ),
            gradient=ft.RadialGradient(
                center=ft.Alignment(0.0, 0.0),
                radius=1.0,
                colors=[
                    "#78d1cd",
                    "#9c96e1"
                ],
                stops=[0.0, 1.0]
            ),
            alignment=ft.alignment.center,
            expand=True
        )

        self.page.add(login_container)
        self.page.update()
