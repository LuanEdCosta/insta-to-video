from argparse import Namespace

MAX_DURATION = 60 * 3


class AppArgs(Namespace):
    def __init__(self):
        # Default Arg Values
        self.music = ""
        self.instagram = ""
        self.duration = 15
        self.number_of_photos = 10
