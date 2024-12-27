import os

def update_kali():
    print("Updating Kali Linux...")
    os.system("sudo apt update && sudo apt full-upgrade -y")
    print("Update completed successfully!")

if __name__ == "__main__":
    update_kali()
