



### 继承type类

```python
commands={}

class CommandType(type):
    def init(cls, name, bases, attrs):
        super(CommandType, cls).init(name, bases, attrs)
        name = getattr(cls, name, cls.name.lower())
        cls.name = name
        if name != 'command':
            commands[name] = cls

Command = CommandType('Command', (object,), {'run': lambda self, args: None})

class Help(Command):
    """Display the list of available commands"""
    def run(self, args):
        print("Available commands:\n")

class Server(Command):
    """Start the odoo server (default command)"""
    def run(self, args):
        print('ssssssssss')

print(commands)

```



