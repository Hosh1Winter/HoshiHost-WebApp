import subprocess, sys, json

def main():
    try:
        subprocess.run([sys.executable,"-m", "pip", "install", "-r", "requirements.txt"])

        print("Dependencies installation done, please input java instilation paths, or leave empty if none")
        loop = True
        jdk8_path = input("Input jdk8: ")
        jdk17_path = input("Input jdk17: ")
        jdk21_path = input("Input jdk21: ")
        while loop:
            try:
                web_port = int(input("Input port for web server: "))
                break
            except:
                print("Not an integer, try again")
        
        print("Now please Input range of ports for the minecraft servers, this will also decide max number of servers")
        while loop:
            try:
                mcserver_pmin = int(input("Min: "))
                break
            except Exception as e:
                print("Not an integer, try again")
        while loop:
            try:
                mcserver_pmax = int(input("Max: "))
                break
            except Exception as e:
                print("Not an integer, try again")
        conf_dictionary = {"jdk8_path":jdk8_path,"jdk17_path":jdk17_path,"jdk21_path":jdk21_path,"web_port":web_port,"mcserver_pmin":mcserver_pmin,"mcserver_pmax":mcserver_pmax}
        with open('config.json', 'w') as conf:
            json.dump(conf_dictionary, conf, indent=4)

        print("\nDone")
    except Exception as e:
        print(f"\nFailed: {e}\n")
    finally:
        input("Press enter to exit: ")

if __name__ == '__main__':
    main()