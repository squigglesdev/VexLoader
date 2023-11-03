import plugins.core.MinecraftProcess as MinecraftProcess
import threading

process = MinecraftProcess.MinecraftProcess()

tickThread = threading.Thread(target=process.tick)
tickThread.start()

commandThread = threading.Thread(target=process.recieveCommand)
commandThread.start()

while True:
    line = process.readLine()
    print(line, end='')
    

    