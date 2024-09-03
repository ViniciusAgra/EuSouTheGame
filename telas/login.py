import flet as ft

class LoginScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

    def on_login_click(self, e):
        username = self.username_field.value
        password = self.password_field.value
        
        # Lógica de verificação do login aqui
        if self.verify_login(username, password):
            # Redireciona para a tela de perfil
            self.navigate("perfil", user_info={"username": username})
        else:
            # Mostra mensagem de erro
            self.page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha incorretos"), bgcolor="#ff0000", open=True)
            self.page.update()

    def on_register_click(self, e):
        # Redireciona para a tela inicial (navegação)
        self.navigate("menu")

    def verify_login(self, username, password):
        # Simulação de verificação de login
        return username == "user" and password == "pass"

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
                    ft.TextButton("Voltar Ao Menu", on_click=self.on_register_click)
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
