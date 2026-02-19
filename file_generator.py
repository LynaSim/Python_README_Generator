from rich.progress import track #progress bar
import time
from rich.console import Console
import logging
from rich.logging import RichHandler

#Initialise RICH console
console = Console()

# Function progress bar simulation
def progress_bar():
    console.print("[bold cyan]Creating your README.md file...[/bold cyan]")
    for _ in track(range(10), description="Processing..."):
        time.sleep(0.2)

# Function for pretty RICH logging information
def setup_logging():
    logging.basicConfig(
        level ="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler()]
    )
    logger = logging.getLogger("rich")
    return logger

# Creates a separate file and appends value of a variable in it
# Adds markdown formatting
def create_file(all_input):
    with open("README.md", "a") as file:
        file.write(f"# {all_input['project_title']}  \n")
        file.write(f"## Description  \n\n{all_input['description']}  \n\n")
        file.write(f"## How to Install  \n\n{all_input['install_instructions']}  \n\n")
        file.write(f"## How to Use  \n\n{all_input['usage_info']}  \n\n")
        file.write(f"## License Type  \n\n{all_input['license']}  \n\n")
        file.write(f"## Author  \n\n{all_input['author']}  \n\n")
        file.write(f"## Contact  \n\n{all_input['contact']}  \n\n")
