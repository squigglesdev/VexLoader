import plugins.core.MinecraftProcess as MinecraftProcess
import threading

process = MinecraftProcess.MinecraftProcess()

tickThread = threading.Thread(target=process.tick)
tickThread.start()