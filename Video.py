from PIL import Image as Img
from PIL import ImageSequence
from Image import Image
from Terminal import Terminal
import time


class Video:
    """
    Video class, made for video stuff
    """

    def __init__(self, video_path: str, break_time: str, size: tuple = None) -> None:
        self.video_path = video_path
        self.video_obj = Img.open(self.video_path)
        self.break_time = float(break_time)
        self.size = size or None

    def show(self) -> None:
        for frame in ImageSequence.Iterator(self.video_obj):
            img = Image(img_object=frame, size=self.size)
            terminal = Terminal(img.size[0])
            my_colors = img.read()
            terminal.print(colors=my_colors, end='\r')
            del terminal
            time.sleep(self.break_time)
