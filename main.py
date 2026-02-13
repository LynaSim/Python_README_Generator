from InquirerPy import inquirer
from InquirerPy.base.control import Choice
# import os

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
print("Thank you for completing this!")

# Create a separate file and write the value of a variable in it
# Add markdown formatting
with open("README.md", "a") as file:
    file.write(f"# {project_title}  \n")
    file.write(f"## Description  \n\n{description}  \n\n")
    file.write(f"## How to Install  \n\n{install_instructions}  \n\n")
    file.write(f"## How to Use  \n\n{usage_info}  \n\n")
    file.write(f"## License Type  \n\n{license}  \n\n")
    file.write(f"## Author  \n\n{author}  \n\n")
    file.write(f"## Contact  \n\n{contact}  \n\n")



