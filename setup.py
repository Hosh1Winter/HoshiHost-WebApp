import subprocess, sys

def main():
    try:
        subprocess.run([sys.executable,"-m", "pip", "install", "-r", "requirements.txt"])
        print("\nAll requirements installed sucessfully")
        input("Press enter to exit: ")
    except Exception as e:
        print(f"\nFailed:{e}")
        input("\nPress enter to exit: ")

if __name__ == '__main__':
    main()