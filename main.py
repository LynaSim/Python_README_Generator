from InquirerPy import inquirer
from InquirerPy.base.control import Choice

project_title = inquirer.text(message="What is your project's title?: ").execute()
print("variable check: " + project_title)
description = inquirer.text(message="Please add a description: ").execute()
print("variable check: " + description)
install_instructions = inquirer.text("Installation instructions: ").execute()
usage_info = inquirer.text(message="How to use: ").execute()
license = inquirer.select(message="Select a license type: ", choices=[
    "Creative Commons license family",
    "Educational Community License v2.0",
    "GNU General Public License family",
    "MIT",
    "Open Software License 3.0"
]).execute()
print("variable check: " + license)
author = inquirer.text(message="Author's name: ").execute()
contact = inquirer.text(message="Contact information: ").execute()
print("Thank you for completing this!")





