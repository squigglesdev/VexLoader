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


    def onLoad(self):
        self.current_time = datetime.now().strftime("%H:%M:%S")
        self.log('Loading config.json', 'Core')
        self.config = self.getConfig()
        self.log('Config loaded!')
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
            for plugin in self.plugins:
                plugin.tick(self, tick)
            time.sleep(1/self.config['tickrate'])



    def sendCommand(self, line):
        self.minecraft_process.sendline(line)

    def readLine(self):
        line = self.minecraft_process.readline()
        if "WARN" in line:
            line = f"\033[93m{line}\033[0m"
        elif "ERROR" in line:
            line = f"\033[91m{line}\033[0m"
        return line
    
    def recieveCommand(self):
        while True:
            line = self.readLine()
            for plugin in self.plugins:
                plugin.recieveCommand(self, line)


    def log(self, line, name):
        print(f"[{self.current_time}] [VexLoader-{name}/INFO]: {line}")

    def warn(self, line, name):
        print(f"\033[93m[{self.current_time}] [VexLoader-{name}/WARN]: {line}\033[0m")

    def error(self, line, name):
        print(f"\033[91m[{self.current_time}] [VexLoader-{name}/ERROR]: {line}\033[0m")