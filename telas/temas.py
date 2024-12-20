import flet as ft
import json

popup_shown = False

class TemasScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate
        global popup_shown

    def create_category_button(self, image_src, tag):
        return ft.TextButton(
            content=ft.Container(
                width=150,
                height=150,
                bgcolor="transparent",
                border_radius=10,
                padding=10,
                margin=10,
                content=ft.Stack(
                    controls=[
                        ft.Image(src=image_src, fit=ft.ImageFit.COVER, width=150, height=150),
                    ]
                )
            ),
            data=tag,
            on_click=self.on_category_button_click,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                overlay_color="transparent"
            )
        )

    def on_category_button_click(self, e):
        tema_selecionado = e.control.data

        with open('data/user_data.json', 'r', encoding='utf-8') as f:
            user_data = json.load(f)

        user_data['temaatual'] = tema_selecionado

        with open('data/user_data.json', 'w', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=4)

        self.navigate("jogo")

    def create_how_to_play_popup(self):
        return ft.AlertDialog(
            modal=True,
            title=ft.Text("Como Jogar:", size=24, weight="bold"),
            content=ft.Column(
                controls=[
                    ft.Text("• Selecione um tema"),
                    ft.Text("• Coloque o celular com a tela virada ao contrário antes da contagem inicial acabar"),
                    ft.Text("• Clique do seu lado Esquerdo (Direito da tela) para contabilizar um acerto"),
                    ft.Text("• Clique do seu lado Direito (Esquerdo da tela) para pular a palavra"),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
                tight=True,
            ),
            actions=[
                ft.TextButton(
                    "Entendi",
                    on_click=self.close_popup
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

    def close_popup(self, e):
        self.page.dialog.open = False
        self.page.update()

    def show_how_to_play_popup(self):
        # Verifica se o popup já foi mostrado
        if not self.popup_shown:
            self.popup_shown = True  # Marca como exibido
            popup = self.create_how_to_play_popup()
            self.page.dialog = popup
            self.page.dialog.open = True
            self.page.update()


    def show(self):
        self.page.title = "Categorias"
        self.page.dialog = self.create_how_to_play_popup()
        self.page.dialog.open = True  # Abre automaticamente
        self.page.update()

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

        banner.content = ft.Row(
            controls=[ft.Image(src="img/BannerCateg.png")],
            alignment=ft.MainAxisAlignment.CENTER
        )

        grid = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.create_category_button("img/categoria_animais.png", "animais"),
                        self.create_category_button("img/categoria_filmes.png", "filme"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    controls=[
                        self.create_category_button("img/categoria_acao.png", "ação"),
                        self.create_category_button("img/categoria_desenhos.png", "desenho"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        content = ft.Column(
            controls=[
                banner,
                grid,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )

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

        self.page.add(main_container)
        self.page.update()

    def create_nav_bar(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.TextButton(
                        "Mais",
                        on_click=self.on_more_click,
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

    def on_more_click(self, e):
        self.navigate("more")

    def on_temas_click(self, e):
        self.navigate("temas")

    def on_configura_click(self, e):
        self.navigate("configura")
