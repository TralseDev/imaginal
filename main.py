#!/usr/bin/python3
### imginal - Image to Terminal written by Tralse ###


from Image import Image
from Video import Video
from Terminal import Terminal
import sys
import argparse


def main(image_path: str, mode: str, break_time: str, size: tuple) -> None:
    if mode == "img":
        img = Image(image_path, size=size)
        my_colors = img.read()
        terminal = Terminal(img.hight)
        terminal.print(my_colors)
    elif mode == "video":
        video = Video(image_path, break_time, size)
        video.show()
    for _ in range(3):
        print()


def main_argparse():
    parser = argparse.ArgumentParser(
        description="View images and videos inside terminal!")
    parser.add_argument("-p", "--path", help="File to show")
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-v", "--video", action="store_true",
                        help="Choose video")
    group1.add_argument("-img", "--image", action="store_true",
                        help="Choose image")
    group2 = parser.add_argument_group()
    group2.add_argument("-b", "--break-time",
                        help="Break between print calls", default=0.07)
    group2.add_argument(
        "-s", "--size", help="Set output size in format: XxY, i.e.: 50x50")
    args = parser.parse_args()

    size = tuple(int(i) for i in args.size.split("x")) if args.size else None
    if len(sys.argv) <= 3:
        print("Invalid number of arguments. Choose -h or --help for help!")
        exit()

    mode = "video" if args.video else "img"
    main(args.path, mode, args.break_time, size)


if __name__ == '__main__':
    main_argparse()
