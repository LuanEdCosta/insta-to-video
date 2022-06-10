from os import makedirs, path, umask
from time import time
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.editor import AudioFileClip

OUTPUT_DIR = "videos"

class VideoMaker:
    def __init__(self, audio_path: str, images_path: str, duration: float, number_of_images: int, user_name: str):
        self.audio_path = audio_path
        self.images_path = images_path
        self.duration = duration
        self.number_of_images = number_of_images
        self.user_name = user_name
        self.create_videos_folder()
        self.create_video()

    def create_videos_folder(self):
        if not path.exists(OUTPUT_DIR):
            umask(0)
            makedirs(OUTPUT_DIR, exist_ok=True)

    def create_video(self):
        fps =  self.number_of_images / self.duration

        audio_clip = AudioFileClip(self.audio_path)
        audio_clip = audio_clip.set_end(self.duration)

        video_clip = ImageSequenceClip(self.images_path, fps=fps)
        video_clip.audio = audio_clip

        video_file_path = "{0}/{1}_{2}.mp4".format(OUTPUT_DIR, self.user_name, int(time()))
        video_clip.write_videofile(video_file_path)
