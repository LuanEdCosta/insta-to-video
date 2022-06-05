from argparse import Namespace


class AppArgs(Namespace):
    def __init__(self) -> None:
        self.music = ""
        self.instagram = ""
        self.duration = 15
        self.number_of_photos = 10
