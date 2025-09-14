import subprocess, sys

def main():
    try:
        subprocess.run([sys.executable,"-m", "pip", "install", "-r", "requirements.txt"])
        print("All requirements installed sucessfully")
    except Exception as e:
        print(f"Failed:{e}")

if __name__ == '__main__':
    main()