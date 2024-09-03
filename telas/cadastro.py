import flet as ft
from database import Database
import logging

logging.basicConfig(
    filename='app.log', 
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger()

class CadastroScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate
        self.db = Database()  # Instancia o banco de dados

    def on_register_click(self, e):
        username = self.username_field.value
        password = self.password_field.value
        
        if username and password:
            try:
                # Tenta adicionar o usuário ao banco de dados
                self.db.add_user(username, password)
                self.page.snack_bar = ft.SnackBar(ft.Text("Cadastro realizado com sucesso"), bgcolor="#008000", open=True)
            except ValueError as ve:
                # Caso o username já exista
                self.page.snack_bar = ft.SnackBar(ft.Text(str(ve)), bgcolor="#ff0000", open=True)
                logger.warning("Usuario Já Existente.")
            except Exception as ex:
                # Caso ocorra outro erro
                self.page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {str(ex)}"), bgcolor="#ff0000", open=True)
                logger.error(f"Erro inesperado ao tentar registrar usuário: {str(ex)}")
        else:
            # Mensagem de erro se os campos não forem preenchidos
            self.page.snack_bar = ft.SnackBar(ft.Text("Por Favor Preencha Todos os Campos Antes de Continuar!"), bgcolor="#ff0000", open=True)
        
        self.page.update()

    def on_menu_click(self, e):
        self.navigate("menu")

    def show(self):
        self.page.title = "Cadastro"

        self.username_field = ft.TextField(label="Usuário", hint_text="Digite seu usuário")
        self.password_field = ft.TextField(label="Senha", hint_text="Digite sua senha", password=True)

        cadastro_container = ft.Container(
            content=ft.Column(
                controls=[
                    self.username_field,
                    self.password_field,
                    ft.ElevatedButton("Registrar", on_click=self.on_register_click),
                    ft.TextButton("Voltar Ao Menu", on_click=self.on_menu_click)
                ],
                alignment="center",
                spacing=20
            ),
            bgcolor="#f0f0f0",
            alignment=ft.alignment.center,
            expand=True
        )

        self.page.add(cadastro_container)
        self.page.update()
