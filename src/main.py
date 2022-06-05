from parser import ArgParser
from youtube import YoutubeDownloader

if __name__ == "__main__":
    arg_parser = ArgParser()
    youtube_downloader = YoutubeDownloader(arg_parser.args.music)
    print(youtube_downloader.audio_full_path)
