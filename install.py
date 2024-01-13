import launch
import os
import git

my_path = os.path.dirname(os.path.realpath(__file__))

# Git Submodule Initialization
with git.Repo(my_path) as repo:
    repo.git.submodule("update", "--init", "--recursive", "--force")
    for submodule in repo.submodules:
        submodule.update(init=True, recursive=True, force=True, keep_going=True)

# Installing Python Dependencies
python_requirements_file = os.path.join(my_path, "requirements.txt")

# Additional command to install bitsandbytes
bitsandbytes_install_command = 'python -m pip install bitsandbytes --index-url=https://jllllll.github.io/bitsandbytes-windows-webui'

# Install all other dependencies from the requirements file
with open(python_requirements_file) as file:
    launch.run_pip(f'{bitsandbytes_install_command} && pip install -r "{python_requirements_file}"', f"sd-webui-train-tools requirement: {python_requirements_file}")
