from PIL import Image
import argparse


"""
将图片转成字符串画：
1. 灰度就是没有色彩，也就是rgb(r, g, b)中三个参数相等
2. 例如灰度级为256的灰度图像，若rgb中三个参数都为100，则代表改点灰度为100
"""


# ascii_char中的字符是根据字符的灰度值由小到大排序的
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)


def get_char(r, g, b, alpha=256):
    """
    1. 获取灰度值gray，一般比率为r:g:b = 3:6:1
    gray = r * 0.3 + g * 0.59 + b + 0.11
    2. 根据灰度值获取到相应字符(gray为灰度值，最大为100，将其对应到字符串上，算出下标)
    gray / 256 = x * len(ascii_char)
    """
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


def main(file_name, out_file_name, width=100, height=100):
    # file_name是图片路径，out_file_name是将图片转成字符串后保存的路径，一般为txt文档
    im = Image.open(file_name)
    # 改变图片像素
    im = im.resize((width, height))
    text = ""
    for i in range(height):
        for j in range(width):
            """getpixel: 获取某个像素位置的rgb值"""
            text += get_char(*im.getpixel((j, i)))
        text += "\n"
    print(text)
    write_file(out_file_name, text)


def write_file(out_file_name, content):
    with open(out_file_name, 'w') as f:
        f.write(content)


def get_params():
    args = argparse.ArgumentParser()
    args.add_argument("-o", "--out_file_name", default="images/test.txt")
    args.add_argument("-f", "--file_name")
    args.add_argument("-W", "--width", type=int, default=100)
    args.add_argument("-H", "--height", type=int, default=100)
    ags = args.parse_args()
    return ags.width, ags.height, ags.file_name, ags.out_file_name


if __name__ == "__main__":
    width, height, file_name, out_file_name = get_params()
    main(file_name=file_name, width=width, height=height, out_file_name=out_file_name)
