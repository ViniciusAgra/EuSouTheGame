import sqlite3

class Database:
    def __init__(self, db_name='Perfis.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Altera a tabela users para adicionar a coluna TempoPartida
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                TempoPartida INTEGER DEFAULT 60  -- Adiciona a nova coluna com valor padrão
            )
        ''')
        self.conn.commit()

    def add_user(self, username, password):
        # Verifica se o username já existe
        self.cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
        if self.cursor.fetchone():
            raise ValueError("Username já existe")

        # Adiciona o usuário se o username não existir
        self.cursor.execute('''INSERT INTO users(username, password, TempoPartida) 
                               VALUES (?, ?, ?)''',  # Inclui TempoPartida na inserção
                               (username, password, 60)  # Define TempoPartida como 60
        )
        self.conn.commit()

    def verify_user(self, username, password):
        self.cursor.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', 
                            (username, password))
        return self.cursor.fetchone() is not None
    
    def get_user_by_username(self, username):
        self.cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
        return self.cursor.fetchone()  # Retorna a linha do usuário ou None se não encontrado
    
    def get_tempo_partida(self, username):
        self.cursor.execute('''SELECT TempoPartida FROM users WHERE username = ?''', (username,))
        result = self.cursor.fetchone()
        return result[0] if result else None  # Retorna o valor ou None se não encontrado


    def close(self):
        self.conn.close()
