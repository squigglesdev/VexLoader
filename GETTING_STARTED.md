# Getting started with VexLoader

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

Each plugin class must have an `onLoad` and `tick` function. These functions take one argument; the minecraft process. The `onLoad` function is called when the plugin is loaded, and the `tick` function is called every tick. 

(**Note:** Plugin ticks are not the same as game ticks! The plugin tick rate can be configured in the `config.json` file.)


```python
class MyPlugin:
    def onLoad(self, process):
        pass

    def tick(self, process):
        pass
```

## Recieving commands

To recieve commands, add a `recieveCommand` function to your plugin class. This function takes two arguments; the minecraft process, and the line. The line is the command that was sent to the server.

```python
class MyPlugin:
    # OnLoad and Tick...

    def recieveCommand(self, process, line):
        if 'Template' in line:
            process.log('Template plugin recieved command!')
            # Note: it is more efficient to use a regex to search for a string
        else:
            pass
```

## Importing modules

Only Python Standard Library modules are allowed to be imported. You can find a list of all Python Standard Library modules [here][python_modules].

[template]: plugins/Template.py
[python_modules]: https://docs.python.org/3/library/