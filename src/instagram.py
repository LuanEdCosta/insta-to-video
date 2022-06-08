from time import time
from os import getenv, makedirs, path
from instagrapi import Client
from dotenv import load_dotenv
from pathlib import Path

OUTPUT_DIR = "images"


class InstagramDownloader:
    def __init__(self, user_name: str, number_of_photos: int):
        self.user_name = user_name
        self.number_of_photos = number_of_photos
        self.downloaded_images_count = 0
        self.user_id = 0
        self.user_output_dir = Path("{0}/{1}_{2}".format(OUTPUT_DIR, user_name, int(time())))
        self.create_output_folder()
        self.download_images()

    def create_output_folder(self):
        if not path.exists(self.user_output_dir):
            makedirs(self.user_output_dir, exist_ok=True)

    def download_images(self):
        client = Client()
        
        load_dotenv()
        INSTAGRAM_USERNAME = getenv("INSTAGRAM_USERNAME")
        INSTAGRAM_PASSWORD = getenv("INSTAGRAM_PASSWORD")
        client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

        self.user_id = client.user_id_from_username(self.user_name)

        end_cursor = None
        while self.downloaded_images_count < self.number_of_photos:
            medias, end_cursor = client.user_medias_paginated(
                self.user_id, self.number_of_photos, end_cursor
            )

            for media in medias:
                if self.downloaded_images_count < self.number_of_photos and media.media_type == 1:
                    client.photo_download(media.pk, self.user_output_dir)
                    self.downloaded_images_count += 1
