from conf.log_conf import log


class CreateDatabaseConnection:
    def start(self):
        log.info(f"Iniciando conexão com base de dados...")
        log.info(f"Conectando ao OracleDB...")
        log.info(f"Rodando migrations...")

    def stop(self):
        log.info(f"Salvando a sessão da Base de dados...")
        log.info(f"Encerrando conexão com OracleDB...")
        asd
        log.info(f"Desconectado da Base com sucesso...")
