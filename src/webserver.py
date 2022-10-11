from conf.log_conf import log


class CreateWebserver:
    def start(self):
        log.info(f"Conectando ao servidor...")
        log.info(f"Aguardando disponibilidade da porta...")

    def stop(self):
        log.info(f"Desconectando do servidor...")
        log.info(f"Fechando a porta antes de sair...")
        log.info(f"Desconectado!")
