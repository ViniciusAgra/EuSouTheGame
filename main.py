import flet as ft

from telas.cadastro import CadastroScreen
from telas.configura import ConfiguraScreen
from telas.login import LoginScreen
from telas.menu import MenuScreen
from telas.personalizado import PersonalizadoScreen
from telas.splash import SplashScreen
from telas.temas import TemasScreen
from telas.jogo import JogoScreen
from database import Database

def main(page: ft.Page):
    db = Database()
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
            JogoScreen(page, navigate).show()
        elif screen == "login":
            LoginScreen(page, navigate).show()
        elif screen == "personalizado":
            PersonalizadoScreen(page, navigate).show()
        elif screen == "temas":
            TemasScreen(page, navigate).show()

    navigate("splash")

ft.app(target=main)