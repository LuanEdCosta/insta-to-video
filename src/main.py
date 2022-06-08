from image import ImageProcessor
from parser import ArgParser
from video import VideoMaker
from youtube import YoutubeDownloader
from instagram import InstagramDownloader

if __name__ == "__main__":
    arg_parser = ArgParser()
    
    youtube_downloader = YoutubeDownloader(
        video_url=arg_parser.args.music
    )
    
    instagram_downloader = InstagramDownloader(
        user_name=arg_parser.args.instagram,
        number_of_photos=arg_parser.args.number_of_photos
    )

    ImageProcessor(
        images_path=instagram_downloader.user_output_dir
    )

    VideoMaker(
        images_path=instagram_downloader.user_output_dir,
        audio_path=youtube_downloader.audio_full_path,
        number_of_images=arg_parser.args.number_of_photos,
        duration=arg_parser.args.duration,
        user_name=arg_parser.args.instagram
    )
