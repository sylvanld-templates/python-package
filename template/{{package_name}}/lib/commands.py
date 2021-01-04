
class CommandHandler:
    def __init__(self, parser):
        self.commands = {}

        self.parser = parser
        self.subparsers = parser.add_subparsers(dest='command')
        
    def register(self, Command):
        command = Command()
        command_parser = command.parser
        self.commands[command_parser.prog] = command
        self.subparsers.add_parser(command_parser.prog, parents=[command_parser], add_help=False)

    def process(self):
        args = self.parser.parse_args()
        self.commands[args.command](args)
