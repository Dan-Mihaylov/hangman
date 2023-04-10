import PIL.Image
from PIL import ImageTk


class CreateImage:

    def __init__(self, path: str):
        self.path = path

    def create_img(self):
        img = PIL.Image.open(self.path)
        image = ImageTk.PhotoImage(img)
        return image
