class Template:
    def onLoad(self, process):
        process.log('Template plugin loaded!')

    def tick(self, process):
        process.log('Template plugin ticked!')

    def recieveCommand(self, process, line):
        if 'Template' in line:
            process.log('Template plugin recieved command!')
            # Note: it is more efficient to use a regex to search for a string
        else:
            pass