from InquirerPy import inquirer
from InquirerPy.base.control import Choice #dropdown
from rich.console import Console
from rich.progress import track #progress bar
import time
import logging
from rich.logging import RichHandler
from input_gathering import get_all_input
from pretty_utils import progress_bar
from pretty_utils import setup_logging
from pretty_utils import display_welcome
from pretty_utils import success_log
from file_generator import create_file

from rich.panel import Panel
from rich import print

console = Console() # Initialise Rich Console

def main():

    # Welcome screen
    display_welcome()

    # Gather all inputs from prompts and store them in dictionary
    all_input = get_all_input()

    # Launches the progress bar before the README is created
    progress_bar()

    # Creates file and write all input to file
    create_file(all_input)

    # Informs of success
    success_log()

if __name__ == "__main__":
    main()

