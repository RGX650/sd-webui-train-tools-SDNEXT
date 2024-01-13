import launch
import os

req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

with open(req_file) as file:
    for lib in file:
        lib = lib.strip()
        if not launch.is_installed(lib):
            launch.run_pip(f"install {lib}", f"clear object requirement: {lib}")

# Install bitsandbytes from the provided wheel URL
bitsandbytes_wheel_url = "https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.41.2.post2-py3-none-win_amd64.whl"
launch.run_pip(f"install {bitsandbytes_wheel_url}", "clear object requirement: bitsandbytes")
