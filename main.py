import flet as ft
import pygame
import time

from telas.cadastro import CadastroScreen
from telas.configura import ConfiguraScreen
from telas.login import LoginScreen
from telas.menu import MenuScreen
from telas.personalizado import PersonalizadoScreen
from telas.splash import SplashScreen
from telas.temas import TemasScreen
from telas.jogo import JogoScreen
from data.database import Database

# Inicializa o Pygame
pygame.mixer.init()

def start_music():
    pygame.mixer.music.load("audio/MTQuemSouEu.mp3")  
    pygame.mixer.music.set_volume(0.1)  
    pygame.mixer.music.play(-1)  

def game_music():
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio\MTQuemSouEu.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1)
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  # Espera 100ms antes de checar novamente

    # Para a segunda música
    pygame.mixer.music.stop()
    pygame.mixer.music.load("audio\MTQuemSouEu.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

def main(page: ft.Page):
    db = Database()
    start_music()  # Inicia a música padrão ao abrir o app

    def navigate(screen, **kwargs):
        page.clean()
        if screen == "splash":
            SplashScreen(page, navigate).show()
        elif screen == "configura":
            ConfiguraScreen(page, navigate).show()
        elif screen == "menu":
            MenuScreen(page, navigate).show()
        elif screen == "cadastro":
            CadastroScreen(page, navigate).show()
        elif screen == "jogo":
            JogoScreen(page, navigate)
            game_music()  # Música para o jogo
        elif screen == "login":
            LoginScreen(page, navigate).show()
        elif screen == "personalizado":
            PersonalizadoScreen(page, navigate).show()
        elif screen == "temas":
            TemasScreen(page, navigate).show()

    navigate("splash")

ft.app(target=main)
