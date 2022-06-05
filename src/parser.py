from argparse import ArgumentParser
from args import AppArgs


class ArgParser:
    def __init__(self):
        self.parser = self.__createParser()
        self.args = self.parser.parse_args(namespace=AppArgs())
        self.__validateArguments(self.args)

    def __createParser(self):
        parser = ArgumentParser(
            description="Use the fotos of an Instagram account to create a short video."
        )

        parser.add_argument(
            "--music",
            "-m",
            type=str,
            metavar="",
            help="The URL or ID of a Youtube video",
            required=True,
        )

        parser.add_argument(
            "--instagram",
            "-i",
            type=str,
            metavar="",
            help="The URL or @ of an Instagram account",
            required=True,
        )

        parser.add_argument(
            "--duration",
            "-d",
            type=float,
            metavar="",
            help="Video duration in seconds",
        )

        parser.add_argument(
            "--number_of_photos",
            "-n",
            type=int,
            metavar="",
            help="The number of photos you want to use in the video",
        )

        return parser

    def __validateArguments(self, args: AppArgs):
        print(args)
