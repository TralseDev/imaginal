from PIL import Image as Img


class OnlyOneArgumentIsAllowed(Exception):
    """
    Error class
    Raises when `img_object` AND `image` path are given
    """


class Image:
    """
    Image class, made for image stuff
    """

    def __init__(self, image: str = '', img_object: Img = None, size: tuple = None) -> None:
        self.image_src = image
        if image and img_object:
            raise OnlyOneArgumentIsAllowed(
                f"Given: image path ({image}) and image object ({img_object}) which is not allowed. Either one or the other.")
        elif image:
            self.image_obj = Img.open(image)
        elif img_object:
            self.image_obj = img_object
        if size:
            self.size = size
            self.image_obj = self.image_obj.resize(size)
        else:
            self.size = self.image_obj.size
        self.hight, self.width = self.size

    def read(self) -> dict:
        # generates rgb values at all pixels
        pixel_values = {}

        for w in range(self.width):
            for h in range(self.hight):
                pixel_values.update({((w, h), self.get_color((h, w)))})

        yield pixel_values

    def get_color(self, pixel: tuple) -> None:
        return self.image_obj.convert('RGB').getpixel(pixel)
