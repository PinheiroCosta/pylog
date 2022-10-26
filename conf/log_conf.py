import logging
from rich.logging import RichHandler


class CustomFormatter(logging.Formatter):

    BLANK_FMT = " "

    # Level
    INFO_FMT = "%(levelname)-9s▶"
    DEBUG_FMT = "[black on white]%(levelname)-9s[/]▶"
    WARNING_FMT = "[black on yellow]%(levelname)-9s[/][yellow]▶[/yellow]"
    ERROR_FMT = "[black on red]%(levelname)-9s[/][red]▶[/red]"
    CRITICAL_FMT = "[black on purple]%(levelname)-9s[/][purple]▶[/purple]"

    # Source
    MODULE_FMT = "[yellow]%(module)-10s[/] "
    FUNCTION_FMT = "[blue]%(funcName)-10s[/] "

    FORMATS = {
        logging.DEBUG: f"{BLANK_FMT*11}{DEBUG_FMT} %(message)s",
        logging.INFO: f"{MODULE_FMT}{INFO_FMT} %(message)s",
        logging.WARNING: f"{MODULE_FMT}{WARNING_FMT} %(message)s",
        logging.ERROR: f"{FUNCTION_FMT}{ERROR_FMT} %(message)s",
        logging.CRITICAL: f"{FUNCTION_FMT}{CRITICAL_FMT} %(message)s"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


DEBUGGER = 0
# Load Colors
if DEBUGGER:
    color_handler = RichHandler(
            log_time_format="[%X]",
            show_level=False,
            rich_tracebacks=True,
            tracebacks_extra_lines=1,
            markup=True
            )
else:
    color_handler = RichHandler(
            log_time_format="[%X]",
            enable_link_path=False,
            show_level=False,
            markup=True
            )

color_handler.setFormatter(CustomFormatter())
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logging.basicConfig(
        filename='log/output.log',
        filemode='a',
        format='%(asctime)s|%(module)s|%(levelname)s|%(message)s',
        datefmt='%x %X')

log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(color_handler)
