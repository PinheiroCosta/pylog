from src.database import CreateDatabaseConnection
from src.webserver import CreateWebserver
from conf.log_conf import log


class CreateCore:
    def __init__(self, config_file=None):
        self.database = CreateDatabaseConnection()
        self.webserver = CreateWebserver()

        if config_file:
            self.database = config_file.database
            self.webserver = config_file.webserver

    def start(self):
        log.info(f"Carregando configurações...")
        try:
            self.database.start()
        except Exception as e:
            log.info(f"Erro ao tentar conectar na base de dados [{e}]")
        else:
            log.info("Conectado na base de dados!")

        try:
            self.webserver.start()
        except Exception as e:
            log.info(f"Erro ao tentar conectar no servidor [{e}]")
        else:
            log.info("Conexão estabelecida com o servidor!")

        log.info(f"Configurações carregadas, Sistema online!")

    def stop(self):
        log.info(f"Parando...")
        self.webserver.stop()
        self.database.stop()
        log.info(f"Finalizado com sucesso!")
