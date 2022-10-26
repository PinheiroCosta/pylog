from src.database import CreateDatabaseConnection
from src.webserver import CreateWebserver
import logging


class CreateCore:
    def __init__(self, config_file=None):
        self.log = logging.getLogger("Core")
        self.database = CreateDatabaseConnection()
        self.webserver = CreateWebserver()

        if config_file:
            self.database = config_file.database
            self.webserver = config_file.webserver

    def load_database(self):
        self.log.info(f"Carregando configurações da base de dados...")
        try:
            self.database.start()
        except Exception as error:
            self.log.error(
                    f"Erro ao tentar conectar na base de dados ({error})",
                    exc_info=True)

            exit(1)
        else:
            self.log.info("Conectado na base de dados!")

    def webserver_connect(self):
        self.log.info(f"Preparando conexao com o Webserver...")
        try:
            self.webserver.start()

        except Exception as error:
            self.log.error(
                    f"Erro ao tentar conectar no servidor ({error})",
                    exc_info=True)
            exit(1)

    def close_database_connection(self):
        self.log.info(f"Encerrando conexão da base de dados com segurança...")
        try:
            self.database.stop()
        except Exception as error:
            self.log.warning(
                    f"Erro encontrado durante o backup da sesão ({error}).",
                    exc_info=True)
        else:
            self.log.info("Backup da sessão realizado com sucesso!")

    def webserver_disconnect(self):
        try:
            self.webserver.stop()
        except Exception as error:
            self.log.warning(
                    f"Não foi possível desconectar do servidor. ({error})",
                    exc_info=True)
        else:
            self.log.info("Desconectado do servidor!")
