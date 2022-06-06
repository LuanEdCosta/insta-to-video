from time import time
from os import makedirs, path
from instagrapi import Client

OUTPUT_DIR = "images"


class InstagramDownloader:
    def __init__(self, user_name: str, number_of_photos: int):
        self.user_name = user_name
        self.number_of_photos = number_of_photos
        self.downloaded_images_count = 0
        self.user_id = 0
        self.user_output_dir = path.abspath("{0}/{1}_{2}".format(OUTPUT_DIR, user_name, int(time())))
        self.create_output_folder()
        self.download_images()

    def create_output_folder(self):
        if not path.exists(OUTPUT_DIR):
            makedirs(OUTPUT_DIR)

    def download_images(self):
        client = Client()
        self.user_id = client.user_id_from_username(self.user_name)

        end_cursor = None
        while self.downloaded_images_count < self.number_of_photos:
            medias, end_cursor = client.user_medias_paginated(
                self.user_id, self.number_of_photos, end_cursor
            )

            for media in medias:
                if media.media_type == 1:
                    client.photo_download(media.pk, self.user_output_dir)
                    self.downloaded_images_count += 1
