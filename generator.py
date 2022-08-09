import os
import cv2
import sys
import argparse
from texture_operations import *
from texture_checks import *
from PIL import Image


def generate_pseudonormal(source_texture, normal_map, replace=False):
    img = Image.open(normal_map).convert('L')
    print("Generating ",normal_map[:len(normal_map)-4]+"_grayscaled.png")
    grayscaled_name = normal_map[:len(normal_map)-4]+"_grayscaled.png"
    try:
        img.save(grayscaled_name)
    except:
        pass
    print("Combining texture and normal map")
    background = cv2.imread(source_texture)
    overlay = cv2.imread(grayscaled_name)
    added_image = cv2.addWeighted(background, 0.92, overlay, 1, 0)
    cv2.imwrite('combined.png', added_image)
    print("Time to fix brightness of result...")
    value = delta_brightness(source_texture, 'combined.png')
    result = change_brightness('combined.png', -1*value)
    cv2.imwrite('combined_result.png', result)
    print("Adjusting saturation...")
    img_pil = adjust_saturation(Image.open('combined_result.png'), 3)
    print("Removing intermediate files")
    os.remove('combined.png')
    os.remove('combined_result.png')
    for i in os.listdir():
        if 'grayscaled' in i:
            os.remove(i)
    if replace:
        img_pil.save(source_texture)
        return True
    print("Prepairing the result: "+source_texture[: len(source_texture) - 4]+'_pseudonormal.png')
    img_pil.save(source_texture[: len(source_texture) - 4]+'_pseudonormal.png')
    print("Done!")
    return True

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--texture', required=True, type=str)
    parser.add_argument('-n', '--nmap', required=True, type=str)
    return parser

def main():
    parser = parse_arguments()
    parameters = parser.parse_args(sys.argv[1:])
    source_texture = format(parameters.texture)
    normal_map = format(parameters.nmap)
    texture_validation(source_texture=source_texture, normal_map=normal_map)
    generate_pseudonormal(source_texture=source_texture, normal_map=normal_map, replace=False)



if __name__=='__main__':
    main()


