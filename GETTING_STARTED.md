# Getting started with VexLoader plugin development

VexLoader makes it very easy to write your own Minecraft plugins. This guide will walk you through the process of writing your first plugin.

You can download the plugin template [here][template]!

## File structure

VexLoader plugins are written in Python. To get started, create a new file in the `plugins` folder. The file name will be the name of your plugin. For example, if you want to name your plugin `MyPlugin`, create a file called `MyPlugin.py` in the `plugins` folder.

## Plugin class

VexLoader plugins are class-based, meaning that you will need to create a class for your plugin. The class name will be the same as the file name. For example, if you want to name your plugin `MyPlugin`, the class name will be `MyPlugin`.

```python
class MyPlugin:
    pass
```

Each plugin class must have an `onLoad` and `tick` method. The `onLoad` method is called when the plugin is loaded, and the `tick` method is called every tick. 

(**Note:** Plugin ticks are not the same as game ticks! The plugin tick rate can be configured in the `config.json` file.)


```python
class MyPlugin:
    def onLoad(self, process):
        pass

    def tick(self, process, tick):
        pass
```

These methods share an argument; the minecraft process. The `tick` method also takes an extra argument; the current tick number. 

## Creating commands

To create a command, you need to register it. You can do this in the `onLoad` method:

```python
class MyPlugin:
    def onLoad(self, process):
        self.myExampleCommand = process.registerCommand('examplecommand', 'ExamplePlugin')
```
The `MinecraftProcess.registerCommand` method takes two arguments; the command name and the plugin name. The command name is the name that the user will type in chat to execute the command. The plugin name is the name of your plugin. This is used to identify which plugin the command belongs to. The method returns the command name, which you can store in a variable if you want.

To handle recieving commands, you need to create a method called `recieveCommand`. This method takes two arguments; the minecraft process and the command:

```python
class MyPlugin:
    # onLoad and tick...

    def recieveCommand(self, process, command):
        if command == self.myExampleCommand:
            process.Log('Recieved command!', 'ExamplePlugin')
```

## Getting online players

To get a list of online players, you can use the `getPlayers` method:

```python
class MyPlugin:
    # onLoad and tick...

    def recieveCommand(self, process, command):
        if command == self.myExampleCommand:
            players = process.getPlayers()
            process.Log('There are ' + str(len(players)) + ' players online!', 'ExamplePlugin')
```
The `MinecraftProcess.getPlayers` method returns a list of player names. This means that you can excecute commands as specific players:

```python
class MyPlugin:
    # onLoad and tick...

    def recieveCommand(self, process, command):
        if command == self.myExampleCommand:
            players = process.getPlayers()
            if "squigglesdev" in players:
                process.executeCommand('say Hello, squigglesdev!', 'ExamplePlugin')
```

## Importing modules

Only Python Standard Library modules are allowed to be imported. You can find a list of all Python Standard Library modules [here][python_modules].

[template]: https://gist.github.com/squigglesdev/71dc83559b30bc21f5a703ab27e1cdfb
[python_modules]: https://docs.python.org/3/library/