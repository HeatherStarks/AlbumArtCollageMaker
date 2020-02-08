from dominantcolors import get_image_dominant_colors
from pathlib import Path
import numpy as np
from PIL import Image
from colorsys import rgb_to_hsv
from math import ceil
from random import randint

class Art:
    """Store path and color information of each image in the collage for sorting"""

    def __init__(self,path):
        self.path = path
        self.dom_col = [255,255,255]

    def grab_color(self):
        dominant_colors = get_image_dominant_colors(image_path=self.path, num_colors=1)
        self.dom_col = dominant_colors[0]

    def __str__(self):
        return str(self.dom_col)

    def __repr__(self):
        return str(self.dom_col)

    def __len__(self):
        return len(self.dom_col)


def color_key_HSV(art):
    return rgb_to_hsv(art.dom_col[0],art.dom_col[1],art.dom_col[2])

def color_key_RGB(art):
    return art.dom_col


def create_image(init_path, out_path, out_name, sort_key_str,ratio,use_perfect_ratio,ratio_fixer, subimage_size=50,format="PNG"):
    """Core function: Gather files in folder, generate object lists and call collage(). Save output"""
    # initialize Directory
    directory = init_path
    png_list = Path(directory).glob('*.png')
    jpg_list = Path(directory).glob('*.jpg')
    art_list = []

    #Create a list of art objects to sort
    for path in png_list:
        new_art = Art(path)
        new_art.grab_color()
        art_list.append(new_art)
    for path in jpg_list:
        new_art = Art(path)
        new_art.grab_color()
        art_list.append(new_art)

    if sort_key_str == 'RGB':
        sort_key = color_key_RGB
    elif sort_key_str == 'HSV':
        sort_key = color_key_HSV
    else:
        sort_key = color_key_HSV


    art_list.sort(key=sort_key)
    list_len = len(art_list)

    ratio_1 = int(ratio[0])
    ratio_2 = int(ratio[1])

    if use_perfect_ratio == False:

        result = collage(list_len,art_list,subimage_size,ratio_1,ratio_2)

    elif use_perfect_ratio == True:
        if ratio_fixer == "stretch":

            result = collage(list_len, art_list, subimage_size, 1, 1)

            newsize = (int(result.size[0]*ratio_1/2),int(result.size[1]*ratio_2/2))

            result.resize(newsize)

        if ratio_fixer == "fill":

            ratio_mult = ratio_1*ratio_2

            tiles_to_add = int(ratio_mult*(ceil(list_len/ratio_mult)**2)-list_len)

            for adds in range(tiles_to_add):
                add_art = Art("fill_square.png")
                rand_pos = randint(1,list_len-1)

                art_list.insert(rand_pos,add_art)

            list_len = len(art_list)

            result = collage(list_len, art_list, subimage_size, ratio_1, ratio_2)

    if format == "PNG":
        result.save(str(out_path + "/" + out_name + '.png'), format="png")
    else:
        result.save(str(out_path + "/" + out_name + '.jpg'), format="jpg")


def collage(list_len,art_list,subimage_size,ratio_1,ratio_2):
    """Helper func for create_image(): perform calculations to organize the collage of desired ratio"""

    factors = []
    for i in range(1, list_len + 1):
        if list_len % i == 0:
            factors.append(i)

    fac_combos = set()
    for factor in range(len(factors) // 2):
        fac_combos.add((factors[factor], factors[-factor - 1]))
        print(fac_combos)

    closest = min(fac_combos, key=lambda x: abs((x[1] / x[0]) - (ratio_1 / ratio_2)))
    print(closest)

    data = np.array([art_list])
    newdata = data.reshape(closest)
    print(newdata)

    image_size = (closest[0] * subimage_size, closest[1] * subimage_size)

    result = Image.new("RGB", image_size)

    for ximg in range(closest[0]):
        for yimg in range(closest[1]):
            current_art = newdata[ximg][yimg]
            current_img = Image.open(current_art.path)
            current_img = current_img.resize((subimage_size, subimage_size))
            result.paste(current_img, (ximg * subimage_size, yimg * subimage_size))

    return result

