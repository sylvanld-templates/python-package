import argparse
from ..lib.hello import format_hello


class SayHello:
    @property
    def parser(self):
        parser = argparse.ArgumentParser("hello", description="Command to say hello to someone!")
        parser.add_argument("dest", help="The one you say hello to...")
        return parser

    def __call__(self, args):
        message = format_hello(args.dest)
        print(message)
