from glob import glob
from PIL import Image

class ImageProcessor:
    def __init__(self, images_path: str):
        self.images_path = images_path
        self.smallest_image = None
        self.need_to_resize = True
        self.find_smallest_image()
        if self.need_to_resize: self.resize_images()

    def find_smallest_image(self):
        width_list = []
        height_list = []

        for filename in glob("{0}/*.jpg".format(self.images_path)):
            image = Image.open(filename)
            width_list.append(image.width)
            height_list.append(image.height)
            if not self.smallest_image or image.width < self.smallest_image[0] or image.height < self.smallest_image[1]:
                self.smallest_image = (image.width, image.height)
        
        if len(list(dict.fromkeys(width_list))) == 1 and len(list(dict.fromkeys(height_list))) == 1:
            self.need_to_resize = False

    def resize_images(self):
        for filename in glob("{0}/*.jpg".format(self.images_path)):
            Image.open(filename).resize(self.smallest_image).save(filename)
