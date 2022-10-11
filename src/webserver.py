import logging


class CreateWebserver:
    def __init__(self):
        self.log = logging.getLogger("Webserver")

    def start(self):
        self.log.info(f"Conectando ao servidor...")
        self.log.info(f"Aguardando disponibilidade da porta...")
        self.log.info(f"Conexão estabelecida!")

    def stop(self):
        self.log.info(f"Desconectando do servidor...")
        self.log.info(f"Fechando a porta antes de sair...")
        self.log.info(f"Desconectado!")
