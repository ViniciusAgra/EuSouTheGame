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

class LoginScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate
        self.db = Database()  # Inicializa o banco de dados

    def on_login_click(self, e):
        username = self.username_field.value
        password = self.password_field.value

        logging.info(f"Botão de login clicado. Usuário: '{username}'")

        # Verifica se o usuário e a senha estão corretos
        if self.verify_login(username, password):
            logging.info(f"Usuário '{username}' fez login com sucesso.")
            self.navigate("Incoporar Tela", user_info={"username": username})
        else:
            logging.warning(f"Tentativa de login falhou para o usuário '{username}'.")
            self.page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha incorretos"), bgcolor="#ff0000", open=True)
            self.page.update()

    def on_menu_click(self, e):
        self.navigate("menu")

    def verify_login(self, username, password):
        # Verifica se o usuário existe e se a senha está correta
        user = self.db.get_user_by_username(username)
        if user and user[2] == password:  # Verifica se a senha corresponde
            logging.info(f"Usuário '{username}' encontrado e senha corresponde.")
            return True
        else:
            logging.info(f"Usuário '{username}' não encontrado ou senha incorreta.")
            return False

    def show(self):
        self.page.title = "Login"

        self.username_field = ft.TextField(label="Usuário", hint_text="Digite seu usuário")
        self.password_field = ft.TextField(label="Senha", hint_text="Digite sua senha", password=True)

        login_container = ft.Container(
            content=ft.Column(
                controls=[
                    self.username_field,
                    self.password_field,
                    ft.ElevatedButton("Login", on_click=self.on_login_click),
                    ft.TextButton("Voltar Ao Menu", on_click=self.on_menu_click)
                ],
                alignment="center",
                spacing=20
            ),
            bgcolor="#f0f0f0",
            alignment=ft.alignment.center,
            expand=True
        )

        self.page.add(login_container)
        self.page.update()
