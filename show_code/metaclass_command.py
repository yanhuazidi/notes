
commands={}

class CommandType(type):
    def __init__(cls, name, bases, attrs):
        super(CommandType, cls).__init__(name, bases, attrs)
        name = getattr(cls, name, cls.__name__.lower())
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

