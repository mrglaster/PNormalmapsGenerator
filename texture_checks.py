import os
import cv2
from PIL import Image

SUPPORTED_TEXTURES = ['.png', '.jpg', '.bmp', '.jpeg']

def is_supportedtexture(filename):
    filename = filename.lower()
    if filename[filename.find("."):] in SUPPORTED_TEXTURES:
        return True
    return False

def existence_check(texture, normalmap):
    if os.path.exists(texture) and os.path.exists(normalmap):
        return True
    print("One or both texture files don't exist. Please check input paths.")
    exit(-1)

def check_sizes(source_texture, normal_map):
    f_source_texture = cv2.imread(source_texture)
    f_normal_map = cv2.imread(normal_map)
    ws, hs, _ = f_source_texture.shape
    wn, hn, _ = f_normal_map.shape
    if ws==wn and hs == hn:
        return True
    print("Normal map and source texture sould have same widht and height")
    print("Your texture resolution: ", ws,'x',hs)
    print("Your normal map resolution: ", wn, 'x', hn)
    exit(-1)

def has_nss(path, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяäößü')):
    return not alphabet.isdisjoint(path.lower())

def texture_path_check(source_texture, normal_map):
    if  ' ' not in source_texture and ' ' not in normal_map  and not has_nss(source_texture) and not has_nss(normal_map):
        return True
    print("Your texture/normal map path contains not supported  symbols. Please change the path(s).")
    exit(-1)

def typo_check(source_texture, normal_map):
    if is_supportedtexture(source_texture) and is_supportedtexture(normal_map):
        return True
    print("Input file types aren't supported by this utility. ")
    print("Supported types: ", end=' ')
    for i in SUPPORTED_TEXTURES:
        print(i, end=" ")
    exit(-1)

def texture_validation(source_texture, normal_map):
    existence_check(texture=source_texture, normalmap=normal_map)
    texture_path_check(source_texture=source_texture, normal_map=normal_map)
    typo_check(source_texture=source_texture, normal_map=normal_map)
    check_sizes(source_texture=source_texture, normal_map=normal_map)
    return True