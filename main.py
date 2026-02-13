from InquirerPy import inquirer

project_title = inquirer.text(message="What is your project's title?: ").execute()
print("variable check: " + project_title)