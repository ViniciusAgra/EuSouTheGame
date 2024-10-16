import sqlite3
import logging

class Database:
    def __init__(self, db_name='Perfis.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        logging.info("Conexão ao banco de dados estabelecida.")
        self.create_tables()  # Adiciona esta chamada

    def create_tables(self):
        # Certifique-se de que a tabela de usuários exista
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            TempoPartida INTEGER DEFAULT 60
        )''')
        self.conn.commit()
        logging.info("Tabela de usuários criada ou já existe.")

    def add_user(self, username, password):
        try:
            self.cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
            self.conn.commit()
            logging.info(f"Usuário '{username}' adicionado com sucesso.")
        except sqlite3.IntegrityError:
            logging.error(f"Erro ao adicionar usuário '{username}': Usuário já existe.")

    def get_user_by_username(self, username):
        self.cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
        return self.cursor.fetchone()

    def get_tempo_partida(self, username):
        self.cursor.execute('''SELECT TempoPartida FROM users WHERE username = ?''', (username,))
        result = self.cursor.fetchone()
        if result:
            logging.info(f"Tempo de partida para '{username}' recuperado: {result[0]} segundos.")
            return result[0]
        logging.warning(f"Usuário '{username}' não encontrado ao tentar obter tempo de partida.")
        return None  # Retorna None se o usuário não for encontrado

    def close(self):
        self.conn.close()
        logging.info("Conexão ao banco de dados fechada.")
