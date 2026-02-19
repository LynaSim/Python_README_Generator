
def get_all_input():

    all_input = {}

    # Questions
    project_title = inquirer.text(
        message="What is your project's title?: ",
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()

    description = inquirer.text(
        message="Please add a description: ", 
        multiline = True,
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()

    install_instructions = inquirer.text(
        message = "Installation instructions: ",
        multiline = True,
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()

    usage_info = inquirer.text(
        message="How to use: ",
        multiline = True,
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip(),
    ).execute()

    license = inquirer.select(
        message="Select a license type: ",
        choices=[
        "Creative Commons license family",
        "Educational Community License v2.0",
        "GNU General Public License family",
        "MIT",
        "Open Software License 3.0"]
    ).execute()

    author = inquirer.text(
        message="Author's name: ",
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()

    contact = inquirer.text(
        message="Contact information: ",
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()