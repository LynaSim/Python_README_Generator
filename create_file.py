# Creates a file and appends variable values
# Adds Markdown formatting
def create_file(all_input):
    with open("README.md", "a") as file:
        file.write(f"# {all_input['project_title']}  \n")
        file.write(f"## Description  \n\n{all_input['description']}  \n\n")
        file.write(f"## How to Install  \n\n{all_input['install_instructions']}  \n\n")
        file.write(f"## How to Use  \n\n{all_input['usage_info']}  \n\n")
        file.write(f"## License Type  \n\n{all_input['license']}  \n\n")
        file.write(f"## Author  \n\n{all_input['author']}  \n\n")
        file.write(f"## Contact  \n\n{all_input['contact']}  \n\n")
