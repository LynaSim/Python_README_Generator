from InquirerPy import inquirer
from InquirerPy.base.control import Choice #dropdown
from rich.console import Console
from rich.progress import track #progress bar
import time
import logging
from rich.logging import RichHandler
from input_gathering import get_all_input
from file_generator import progress_bar
from file_generator import create_file
from file_generator import setup_logging


console = Console()
setup_logging() # Loads the pretty logging utility
logger = setup_logging() # activates logger function

# Gather all inputs from prompts and store them in dictionary
all_input = get_all_input()
print(f"This is the value of dictionary all_input: {all_input}")

# Launches the progress bar before the README is created
progress_bar()

# Creates file and write all input to file
create_file(all_input)

# Informs of success
logger.info("Your README.md file was successfully created!")

