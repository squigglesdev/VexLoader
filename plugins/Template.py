class Template:
    def onLoad(self, process):
        process.log('Template plugin loaded!', 'Template')

    def tick(self, process, tick):
        process.log('Template plugin ticked!', 'Template')

    def recieveCommand(self, process, line):
        if 'Template' in line:
            process.log('Template plugin recieved command!', 'Template')
            # Note: it is more efficient to use a regex to search for a string
        else:
            pass