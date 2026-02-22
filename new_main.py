from InquirerPy import inquirer
from InquirerPy.base.control import Choice #dropdown
from rich.console import Console
from input_gathering import get_all_input
from pretty_utils import progress_bar, display_welcome, success_log
from file_generator import create_file

console = Console() # Initialise Rich Console

def main():

    # Welcome screen
    display_welcome()

    # Gather all inputs from prompts and store them in dictionary
    all_input = get_all_input()

    # Launches the progress bar before file is created
    progress_bar()

    # Creates file and writes all input to file
    create_file(all_input)

    # Informs of success
    success_log()

if __name__ == "__main__":
    main()

