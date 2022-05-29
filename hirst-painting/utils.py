import colorgram


def convert_to_rgb(color):
    return color.rgb.r, color.rgb.g, color.rgb.b


colours = colorgram.extract('image.jpg', 30)
COLOURS = [convert_to_rgb(color) for color in colours]
