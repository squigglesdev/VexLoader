import os
import json
import importlib
import time
from datetime import datetime
import threading


if os.name == 'nt':
    import wexpect as pexpect
elif os.name == 'posix':
    import pexpect as pexpect
else:
    print('Unsupported OS')
    exit(1)

class MinecraftProcess:

    def __init__(self):
        self.onLoad()


    def getConfig(self):
        with open('config.json') as f:
            return json.load(f)
        
    def getPlugins(self):
        self.pluginPaths = []
        self.plugins = []
        for file in os.listdir('plugins'):
            if file.endswith('.py'):
                self.pluginPaths.append(file[:-3])
        for i in self.pluginPaths:
            module = importlib.import_module(f'plugins.{i}')
            class_ = getattr(module, i)
            self.plugins.append(class_())

    def registerCommand(self, command, plugin):
        self.commands.append(f"{command}({plugin})")
        self.log(f'Registered command {command} from plugin {plugin}!', 'Core')
        return command


    def onLoad(self):
        self.commands = []
        self.current_time = datetime.now().strftime("%H:%M:%S")
        self.log('Loading config.json', 'Core')
        self.config = self.getConfig()
        self.log('Config loaded!', 'Core')
        self.log(f'Starting Minecraft process...', 'Core')
        self.minecraft_process = pexpect.spawn(f"java -Xmx{self.config['memory']} -jar {self.config['serverpath']} nogui", encoding='utf-8', timeout=None)
        self.log('Minecraft process loaded!', 'Core')
        self.log('Loading plugins...', 'Core')
        self.getPlugins()
        for plugin in self.plugins:
            plugin.onLoad(self)
        self.log('Plugins loaded!', 'Core')   


    def tick(self):
        while True:
            tick = datetime.now()
            self.current_time = datetime.now().strftime("%H:%M:%S")
            line = self.readLine()
            print(line, end='')
            for plugin in self.plugins:
                plugin.tick(self, tick)
            for command in self.commands:
                plugin_name = command.split('(')[1][:-1]
                command_name = command.split('(')[0]
                
                if command_name in line:
                    self.log(f"Received command {command_name} from plugin {plugin_name}!", 'Core')
                    for plugin in self.plugins:
                        if plugin_name in str(plugin):
                            pluginCommandThread = threading.Thread(target=plugin.recieveCommand, args=(self, command_name))
                            pluginCommandThread.start()
            time.sleep(1 / self.config['tickrate'])


    def sendCommand(self, line):
        self.minecraft_process.sendline(line)

    def readLine(self):
        index = self.minecraft_process.expect(['\r\n', pexpect.EOF, pexpect.TIMEOUT], timeout=0.1)
        if index == 0:
            line = self.minecraft_process.before + '\r\n'
        elif index == 1:
            self.log('Minecraft process closed!', 'Core')
            self.minecraft_process.close()
        elif index == 2:
            line = ""
        else:
            line = self.minecraft_process.before

        if "WARN" in line:
            line = f"\033[93m{line}\033[0m"
        elif "ERROR" in line:
            line = f"\033[91m{line}\033[0m"
        return line


    def log(self, line, name):
        print(f"[{self.current_time}] [VexLoader-{name}/INFO]: {line}")

    def warn(self, line, name):
        print(f"\033[93m[{self.current_time}] [VexLoader-{name}/WARN]: {line}\033[0m")

    def error(self, line, name):
        print(f"\033[91m[{self.current_time}] [VexLoader-{name}/ERROR]: {line}\033[0m")