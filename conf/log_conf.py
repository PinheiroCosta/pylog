import logging
from rich.logging import RichHandler


class CustomFormatter(logging.Formatter):

    # Formatting Configuration
    MODULE_FMT = "[yellow]%(module)+10s[/] "

    INFO_FMT = "%(levelname)-8s▶"
    DEBUG_FMT = "[black on white]%(levelname)s[/]▶"
    WARNING_FMT = "[black on yellow]%(levelname)-8s[/][yellow]▶[/yellow]"
    ERROR_FMT = "[black on red]%(levelname)-8s[/][red]▶[/red]"
    CRITICAL_FMT = "[black on purple]%(levelname)-8s[/][purple]▶[/purple]"

    FORMATS = {
        logging.DEBUG: f"{MODULE_FMT}{DEBUG_FMT} %(message)s",
        logging.INFO: f"{MODULE_FMT}{INFO_FMT} %(message)s",
        logging.WARNING: f"{MODULE_FMT}{WARNING_FMT} %(message)s",
        logging.ERROR: f"{MODULE_FMT}{ERROR_FMT} %(message)s",
        logging.CRITICAL: f"{MODULE_FMT}{CRITICAL_FMT} %(message)s"
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
