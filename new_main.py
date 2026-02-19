from InquirerPy import inquirer
from InquirerPy.base.control import Choice #dropdown
from rich.console import Console
from rich.progress import track #progress bar
import time
import logging
from rich.logging import RichHandler
from input_gathering import get_all_input
from file_generator import creating_file_simulation
from file_generator import create_file


# Gather all inputs from prompts and store them in dictionary
all_input = get_all_input()
print(f"This is the value of dictionary all_input: {all_input}")

# Launches the progress bar before the README is created
creating_file_simulation()

# # Function for pretty RICH logging information
# def setup_logging():
#     logging.basicConfig(
#         level ="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
#     )
#     logger = logging.getLogger("rich")
#     return logger

# logger = setup_logging()

# Creates file and write all input to file
create_file(all_input)