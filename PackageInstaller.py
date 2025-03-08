import subprocess
import sys

# List of packages to install
packages = ['pandas', 'numpy', 'math', 'folium']

# Function to install the packages
def install_packages(packages):
    for package in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Install the packages
install_packages(packages)

print("Packages installed successfully.")