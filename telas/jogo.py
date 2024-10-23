import flet as ft
import random
import json
import time
import threading  # Para executar o countdown em uma thread separada

class JogoScreen:
    def __init__(self, page: ft.Page, navigate):
        self.page = page
        self.navigate = navigate

        self.build_ui()  # Constrói a interface

    def build_ui(self):
        # Adicionando o gradiente de fundo
        gradient_background = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=["#e5f6f8", "#f2feff"]
            ),
            expand=True,  # Preenche todo o espaço disponível
        )

        # Carregar palavras do JSON
        with open('data/temas_base.json', 'r', encoding='utf-8') as f:
            self.temas = json.load(f)

        # Selecionar tema 'filme'
        self.palavras_filme = self.temas['filme']['palavras']
        self.palavra_atual = random.choice(self.palavras_filme)

        # Timer de 60 segundos
        self.timer = 60

        # Container para o banner superior
        header_banner = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, 0),
                end=ft.Alignment(1, 0),
                colors=["#93e4ed", "#e7baff", "#93e4ed"]
            ),
            width=self.page.width,
            height=100,
            alignment=ft.alignment.center
        )

        # Container central para exibir a palavra
        self.palavra_container = ft.Container(
            content=ft.Text(self.palavra_atual, size=40, color="#8c68ca"),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.TRANSPARENT,
            expand=True,
        )

        # Criar banner para o timer
        self.timer_text = ft.Text(f"Tempo restante: {self.timer}s", size=20)

        banner = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, 0),
                end=ft.Alignment(1, 0),
                colors=["#93e4ed", "#e7baff", "#93e4ed"]
            ),
            width=self.page.width,
            height=100,
            alignment=ft.alignment.center,
            content=self.timer_text
        )

        # Criar GestureDetectors invisíveis para cada metade da tela
        left_detector = ft.GestureDetector(
            content=ft.Container(
                expand=True,
                bgcolor=ft.colors.TRANSPARENT,
            ),
            on_tap=self.handle_click_left,
        )

        right_detector = ft.GestureDetector(
            content=ft.Container(
                expand=True,
                bgcolor=ft.colors.TRANSPARENT,
            ),
            on_tap=self.handle_click_right,
        )

        # Stack para organizar a interface
        main_stack = ft.Stack(
            controls=[
                gradient_background,  # Gradiente de fundo
                header_banner,        # Banner no topo
                self.palavra_container,
                # Adiciona o banner na parte inferior
                ft.Container(
                    content=banner,
                    alignment=ft.alignment.bottom_center,
                ),
                left_detector,  # Detector para a esquerda
                right_detector  # Detector para a direita
            ],
            expand=True,
        )

        self.page.add(main_stack)  # Adiciona a interface à página

        # Inicia o timer em uma thread separada
        timer_thread = threading.Thread(target=self.countdown, args=(self.timer,))
        timer_thread.start()

    def handle_click_left(self, e: ft.ControlEvent):
        self.errou()

    def handle_click_right(self, e: ft.ControlEvent):
        self.acertou()

    def acertou(self):
        self.mudar_palavra()

    def errou(self):
        self.mudar_palavra()

    def mudar_palavra(self):
        self.palavra_atual = random.choice(self.palavras_filme)
        self.palavra_container.content = ft.Text(self.palavra_atual, size=40, color="#8c68ca")
        self.page.update()

    def countdown(self, t):
        while t:
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.timer_text.value = f"Tempo restante: {timer}"
            self.page.update()
            time.sleep(1)
            t -= 1

        self.timer_text.value = "Tempo esgotado!"
        self.page.update()
