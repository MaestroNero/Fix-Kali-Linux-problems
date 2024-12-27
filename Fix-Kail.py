import os

def create_fix_file():

    script_content = """# Kali-Linux
import os


os.system('sudo apt update')
os.system('sudo apt full-upgrade -y')
"""

if __name__ == "__main__":
    create_fix_file()
