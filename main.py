from InquirerPy import inquirer
from InquirerPy.base.control import Choice #dropdown
from rich.console import Console
from rich.progress import track #progress bar
import time
import logging
from rich.logging import RichHandler

#Initialise RICH console
console = Console()

# Questions
project_title = inquirer.text(message="What is your project's title?: ").execute()
description = inquirer.text(message="Please add a description: ").execute()
install_instructions = inquirer.text("Installation instructions: ").execute()
usage_info = inquirer.text(message="How to use: ").execute()
license = inquirer.select(message="Select a license type: ", choices=[
    "Creative Commons license family",
    "Educational Community License v2.0",
    "GNU General Public License family",
    "MIT",
    "Open Software License 3.0"
]).execute()
author = inquirer.text(message="Author's name: ").execute()
contact = inquirer.text(message="Contact information: ").execute()

# Function progress bar simulation
def creating_file_simulation():
    console.print("[bold cyan]Creating your README.md file...[/bold cyan]")
    for _ in track(range(10), description="Processing..."):
        time.sleep(0.2)

# Launches the progress bar before the README is created
creating_file_simulation()

# Function for pretty RICH logging information
def setup_logging():
    logging.basicConfig(
        level ="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
    )
    logger = logging.getLogger("rich")
    return logger

logger = setup_logging()

# Creates a separate file and appends value of a variable in it
# Adds markdown formatting
with open("README.md", "a") as file:
    file.write(f"# {project_title}  \n")
    file.write(f"## Description  \n\n{description}  \n\n")
    file.write(f"## How to Install  \n\n{install_instructions}  \n\n")
    file.write(f"## How to Use  \n\n{usage_info}  \n\n")
    file.write(f"## License Type  \n\n{license}  \n\n")
    file.write(f"## Author  \n\n{author}  \n\n")
    file.write(f"## Contact  \n\n{contact}  \n\n")
    logger.info("Your README.md file was successfully created!")



