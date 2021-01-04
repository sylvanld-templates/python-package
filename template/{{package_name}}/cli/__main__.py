import argparse
from .hello import SayHello
from ..lib.commands import CommandHandler


def main():
    parser = argparse.ArgumentParser("{{package_name}}", description="{{package_description}}")
    handler = CommandHandler(parser)

    handler.register(SayHello)

    handler.process()
