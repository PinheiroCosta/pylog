#!/usr/bin/env python3
from src.core import CreateCore
from conf.log_conf import log


core = CreateCore()


if __name__ == "__main__":
    try:
        print()
        log.info("Iniciando Programa...")
        core.start()

        print()
        core.stop()

    except Exception as e:
        log.error(f"Erro desconhecido ({e}).")

    else:
        log.info("Programa parado com sucesso.")
