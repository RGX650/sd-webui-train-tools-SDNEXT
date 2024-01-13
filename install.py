import os
import launch
import git
import zipfile

# Determine the path to the current script file
script_path = os.path.realpath(__file__)
script_directory = os.path.dirname(script_path)

# Download the ZIP file containing the tar.gz file
zip_file_url = "https://github.com/wkpark/bitsandbytes/actions/runs/7117279173/artifacts/1096989694"
zip_file_name = "bitsandbytes-windows-latest-12.1.zip"
launch.run(f'curl -LJO {zip_file_url} -o {zip_file_name}', "Downloading ZIP file")

# Extract the ZIP file using Python's zipfile module
with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    zip_ref.extractall(script_directory)

# Determine the name of the extracted folder
extracted_folder = f'{os.path.splitext(zip_file_name)[0]}'

# Navigate to the extracted folder
os.chdir(os.path.join(script_directory, extracted_folder))

# Navigate to the extracted folder
os.chdir(os.path.join(script_directory, extracted_folder))

# Extract the tar.gz file
tar_file_name = "bitsandbytes-0.41.2.tar.gz"
launch.run(f'tar -xzvf {tar_file_name}', "Extracting tar.gz file")

# Determine the name of the extracted folder
extracted_folder = f'{os.path.splitext(zip_file_name)[0]}'

# Navigate to the extracted folder
os.chdir(os.path.join(script_directory, extracted_folder))

# Extract the tar.gz file
tar_file_name = "bitsandbytes-0.41.2.tar.gz"
launch.run(f'tar -xzvf {tar_file_name}', "Extracting tar.gz file")

# Determine the name of the extracted tar.gz folder
extracted_tar_folder = f'{os.path.splitext(tar_file_name)[0]}'

# Navigate to the extracted tar.gz folder
os.chdir(os.path.join(script_directory, extracted_tar_folder))

# Install the package using pip
launch.run_pip("install .", "Installing bitsandbytes package --prefer-binary")

# Navigate back to the script directory
os.chdir(script_directory)

# Get the path to the requirements.txt file
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

# Open the requirements.txt file and process each line
with open(req_file) as file:
    for lib in file:
        lib = lib.strip()

        # Check if the package is from a GitHub repository
        if lib.startswith("git+"):
            # Install the GitHub repository package
            git_repo_url = lib[len("git+"):]
            repo_name = os.path.basename(git_repo_url.rstrip(".git"))
            install_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), repo_name)
            
            if not os.path.exists(install_path):
                git.Repo.clone_from(git_repo_url, install_path)

            launch.run_pip(f'install -e {install_path}', f"clear object requirement: {lib}")
        elif not launch.is_installed(lib):
            # Install other packages from PyPI if not already installed
            launch.run_pip(f'install {lib}', f"clear object requirement: {lib}")
