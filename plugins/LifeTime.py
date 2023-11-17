import time
import re

class LifeTime:
        
    def onLoad(self, process):
        process.log('LifeTime plugin loaded!', 'LifeTime')
        self.resett10 = process.registerCommand('resett10', 'LifeTime')
        self.test = process.registerCommand('TEST', 'LifeTime')

    def tick(self, process, tick):
        pass


    def recieveCommand(self, process, command):
        if command == self.resett10:
            process.log('Resett10 command recieved!', 'LifeTime')
            time.sleep(1)
            process.sendCommand('tick freeze')
            time.sleep(3)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.tick hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "10", "color": "aqua"}')
            time.sleep(1)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.tick hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "9", "color": "aqua"}')
            time.sleep(1)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.tick hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "8", "color": "aqua"}')
            time.sleep(1)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.tick hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "7", "color": "aqua"}')
            time.sleep(1)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.tick hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "6", "color": "aqua"}')
            time.sleep(1)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.tick hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "5", "color": "aqua"}')
            time.sleep(1)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.tick hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "4", "color": "aqua"}')
            time.sleep(1)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.tick hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "3", "color": "aqua"}')
            time.sleep(1)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.tick hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "2", "color": "aqua"}')
            time.sleep(1)
            process.sendCommand("execute as @a at @a run playsound slowmo:slowmo.end hostile @a ~ ~ ~")
            process.sendCommand('execute as @a at @a run title @a actionbar {"text": "1", "color": "aqua"}')
            time.sleep(2)
            process.sendCommand("function slowmo:resettick")
        elif command == self.test:
            process.log('TEST command recieved!', 'LifeTime')
            time.sleep(1)
            players = process.getPlayers()
            if "Squigglybark357" in players:
                process.sendCommand(f'execute as Squigglybark357 at Squigglybark357 run say hi from squigglybark357')
            process.sendCommand(f'execute as @a at @a run title @a actionbar {{"text": "{players}", "color": "aqua"}}')

        else:
            pass
