import flet as ft

class CadastroScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

    def on_register_click(self, e):
        username = self.username_field.value
        password = self.password_field.value
        
        if username and password:
            # Simula a adição de usuário
            # self.db.add_user(username, email, password)
            self.page.snack_bar = ft.SnackBar(ft.Text("Cadastro realizado com sucesso"), bgcolor="#008000", open=True)
            self.page.update()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Por Favor Preencha Todos os Campos Antes de Continuar!"), bgcolor="#ff0000", open=True)
            self.page.update()

    def on_login_click(self, e):
        # Redireciona para a tela inicial (navegação)
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
                    ft.TextButton("Voltar Ao Menu", on_click=self.on_login_click)
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
