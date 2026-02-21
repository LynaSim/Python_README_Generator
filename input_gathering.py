from InquirerPy import inquirer

def get_all_input():

    all_input = {}

    # Questions
    all_input['project_title']= inquirer.text(
        message="What is your project's title?: ",
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()

    all_input['description'] = inquirer.text(
        message="Please add a description: ", 
        multiline = True,
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()

    all_input['install_instructions'] = inquirer.text(
        message = "Installation instructions: ",
        multiline = True,
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()

    all_input['usage_info'] = inquirer.text(
        message="How to use: ",
        multiline = True,
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip(),
    ).execute()

    all_input['license'] = inquirer.select(
        message="Select a license type: ",
        choices=[
        "Creative Commons license family",
        "Educational Community License v2.0",
        "GNU General Public License family",
        "MIT",
        "Open Software License 3.0"]
    ).execute()

    all_input['author'] = inquirer.text(
        message="Author's name: ",
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()

    all_input['contact'] = inquirer.text(
        message="Contact information: ",
        validate = lambda result: len(result.strip()) > 0,
        invalid_message = "Input cannot be empty.",
        filter=lambda result: result.strip()
    ).execute()

    return all_input #important