from pytube import YouTube

OUTPUT_DIR = "audios"

class YoutubeDownloader:
    def __init__(self, video_url: str):
        self.video_url = video_url
        self.audio_full_path = self.download()

    def download(self) -> str:
        yt = YouTube(self.video_url)
        streams = yt.streams.filter(only_audio=True)

        if not streams:
            print("No audio stream found to download")
            exit(1)

        # TODO: Create option to select the audio quality
        first_stream = streams[0]

        path = first_stream.download(
            output_path=OUTPUT_DIR, filename="{0}.mp4".format(yt.video_id)
        )

        return path
