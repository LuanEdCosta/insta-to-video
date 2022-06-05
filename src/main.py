from instagram import InstagramDownloader
from parser import ArgParser
from youtube import YoutubeDownloader

if __name__ == "__main__":
    arg_parser = ArgParser()
    youtube_downloader = YoutubeDownloader(arg_parser.args.music)
    instagram_downloader = InstagramDownloader(
        arg_parser.args.instagram, arg_parser.args.number_of_photos
    )
