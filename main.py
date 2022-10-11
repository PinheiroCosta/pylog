#!/usr/bin/env python3
from src.core import CreateCore
from conf.log_conf import log


def core_start():
    try:
        print()
        log.info("Iniciando Programa...")
        core.load_database()
        core.webserver_connect()
    except Exception as error:
        log.error(f"Erro durante inicialização ({error}).", exc_info=True)
    else:
        log.info(f"Configurações carregadas, Sistema online!")
        print()


def core_stop():
    try:
        core.webserver_disconnect()
        core.close_database_connection()

    except Exception as e:
        log.error(f"Erro durante o encerramento ({e}).", exc_info=True)

    else:
        log.info("Programa parado com sucesso.")


core = CreateCore()


if __name__ == "__main__":

    core_start()
    core_stop()
