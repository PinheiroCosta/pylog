import logging


class CreateDatabaseConnection:
    def __init__(self):
        self.log = logging.getLogger("Database")

    def start(self):
        self.log.info(f"Iniciando conexão com base de dados...")
        self.log.info(f"Conectando ao OracleDB...")
        self.log.info(f"Rodando migrations...")

    def stop(self):
        self.log.info(f"Salvando a sessão da Base de dados...")
        self.log.info(f"Encerrando conexão com OracleDB...")
        self.log.info(f"Desconectado da Base com sucesso...")
