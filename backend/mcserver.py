import subprocess, platform, json, os

#imports commands.json, this file has all the commands that could ever be run, if your device requires somthing to be changed, do it there
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, 'data', 'commands.json')
with open(path, 'r') as database:
        commands = json.load(database)

def find_server_path(usr_email): #Finds the path for the server based on email
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, 'data', 'servers', usr_email.replace('@','_at_').replace('.','_'))
    return path

class Server():
    def __init__(self, _name, _usr_email, jdk_version):
        self.name = _name
        self.path = find_server_path(_usr_email)
        self.version = jdk_version
        self.process = None

    def build_start_command(self, config):
        if platform.system() == "Windows":
             server_platform = "Windows"
        elif platform.system() == "Linux":
            if "aarch" in platform.machine().lower():
                 server_platform = "Linux-Arm"
            else:
                 server_platform = "Linux"
        print(server_platform)
        
        command = commands[server_platform + '_Start'][self.version]
        if config[f"{self.version}_path"] == "":
             pass
        else:
            command[0] = config[f"{self.version}_path"]
        print(f"running with {self.version}, at {command[0]}, if that is wrong check server version and config")
        return command
        



    def start(self, config):
        #starts the server and stores process as self.process
        try:
            self.process = subprocess.Popen(self.build_start_command(config), cwd=self.path)
        except Exception as e:
             print(f"Error{e}")

    def force_stop(self):
        #force stops the server incase you can't run 'stop' in the minecraft console
        pass


#imports commands.json, this file has all the commands that could ever be run, if your device requires somthing to be changed, do it there
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, 'data', 'commands.json')
with open(path, 'r') as database:
        commands = json.load(database)