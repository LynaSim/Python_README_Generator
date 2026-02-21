from rich.progress import track #progress bar
import time
from rich.console import Console
import logging
from rich.logging import RichHandler
from rich.panel import Panel
from rich import print
from rich.text import Text

#Initialise RICH console
console = Console()

def display_welcome():
    console.print(
        Panel(
            Text("\n README.md GENERATOR", justify="center"),
            title="Welcome",
            subtitle="Made with Python, InquirerPy and Rich",
            height=5
            )
        )

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

# Creates a separate file and appends value of a variable to it
# Adds Markdown formatting
def create_file(all_input):
    with open("README.md", "a") as file:
        file.write(f"# {all_input['project_title']}  \n")
        file.write(f"## Description  \n\n{all_input['description']}  \n\n")
        file.write(f"## How to Install  \n\n{all_input['install_instructions']}  \n\n")
        file.write(f"## How to Use  \n\n{all_input['usage_info']}  \n\n")
        file.write(f"## License Type  \n\n{all_input['license']}  \n\n")
        file.write(f"## Author  \n\n{all_input['author']}  \n\n")
        file.write(f"## Contact  \n\n{all_input['contact']}  \n\n")
