from argparse import ArgumentParser
from args import MAX_DURATION, AppArgs
from utils import is_url


class ArgParser:
    def __init__(self):
        self.parser = self.__create_parser()
        self.args = self.parser.parse_args(namespace=AppArgs())
        self.__format_arguments()

    def __create_parser(self):
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

    def __format_arguments(self):
        if is_url(self.args.music):
            if not "youtube.com" in self.args.music:
                print("--music option is not a valid Youtube URL")
                exit(1)
        else:
            self.args.music = "https://youtube.com/watch?v={0}".format(self.args.music)

        if is_url(self.args.instagram):
            if "instagram.com" in self.args.instagram:
                self.args.instagram = (
                    self.args.instagram.removesuffix("/").split("/").pop()
                )
            else:
                print("--instagram option is not a valid Instagram URL")
                exit(1)

        if self.args.duration > MAX_DURATION:
            print(
                "--duration option is invalid. The max duration is: {0} seconds".format(
                    MAX_DURATION
                )
            )
            exit(1)
