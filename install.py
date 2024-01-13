import os
import launch

# Download the ZIP file containing the tar.gz file
zip_file_url = "https://github.com/wkpark/bitsandbytes/actions/runs/7117279173/artifacts/1096989694"
zip_file_name = "bitsandbytes-windows-latest-12.1.zip"
launch.run(f'curl -LJO {zip_file_url} -o {zip_file_name}', "Downloading ZIP file")

# Extract the ZIP file
launch.run(f'unzip {zip_file_name}', "Extracting ZIP file")

# Navigate to the extracted folder
extracted_folder = f'{os.path.splitext(zip_file_name)[0]}'
os.chdir(extracted_folder)

# Extract the tar.gz file
tar_file_name = "bitsandbytes-0.41.2.tar.gz"
launch.run(f'tar -xzvf {tar_file_name}', "Extracting tar.gz file")

# Navigate to the extracted folder
extracted_tar_folder = f'{os.path.splitext(tar_file_name)[0]}'
os.chdir(extracted_tar_folder)

# Install the package using pip
launch.run_pip("install .", "Installing bitsandbytes package")

# Get the path to the requirements.txt file
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

# Open the requirements.txt file and process each line
with open(req_file) as file:
    for lib in file:
        lib = lib.strip()

        # Check if the package is from a GitHub repository
        if lib.startswith("git+"):
            # Install the GitHub repository package
            launch.run_pip(f"install {lib}", f"clear object requirement: {lib}")
        elif not launch.is_installed(lib):
            # Install other packages from PyPI if not already installed
            launch.run_pip(f"install {lib}", f"clear object requirement: {lib}")
