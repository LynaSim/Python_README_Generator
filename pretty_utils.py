from rich.progress import track #progress bar
import time
from rich.console import Console
import logging
from rich.logging import RichHandler
from rich.panel import Panel
from rich import print
from rich.text import Text

# Initialise RICH console
console = Console()

# Welcome screen
def display_welcome():
    console.print(
        Panel(
            Text("\n README.md GENERATOR", style="yellow", justify="center"),
            title="[magenta]Welcome to my[/]",
            subtitle="[magenta]Made with Python:snake:, InquirerPy and Rich[/]",
            height=5,
            border_style="yellow"
            )
        )
    console.input("\n [yellow dim]Press Enter to start.[/]")


# Function progress bar simulation
def progress_bar():
    console.print("[bold cyan]Creating your README.md file...[/bold cyan]")
    for _ in track(range(20), description="[bold green]Processing..."):
        time.sleep(0.1)


# Tells Python to hand the logging job to Rich
def setup_logging():
    logging.basicConfig(
        level ="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(markup = True)],
    )
    logger = logging.getLogger("rich")
    return logger


# Success log to confirm file created
def success_log():
    logger = setup_logging() #  Initialise Rich Logging
    logger.info(":white_heavy_check_mark: [bold on green1] SUCCESS! [/] [yellow]Your README.md is ready![/]:sparkles::sparkles:")