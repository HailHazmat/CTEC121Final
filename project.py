# project.py
# Matthew Bade

# My Final project for this class, a program that uses a user entered term to find images and convert them into a collage dynamically.

from google_images_search import GoogleImagesSearch
from PIL import Image
import random
import sys

# verifies my GoogleImagesSearch object with my API key and custom search engine ID
gis = GoogleImagesSearch('AIzaSyBUNxiSzqRPTmIHNoH55wiSB9kEOZpWIlw', 'd6a1744a684d948b7')

def main():
    user_search = input("Enter a search term: ")
    images_info = search_images(user_search)
    collage = create_collage(images_info)
    save_collage(collage, 'output.png')
    print("Collage created and saved as output.png")


def search_images(search_term, download_path="/path/", num_results=4):
    # saves the first 4 images to a path
    # limits images to 4 for the collage
    # search parameters with dynamic search term and attributes, modified from the API's recommended search settings
    _search_params = {
        'q': search_term,
        'num': num_results,
        'fileType': 'png',
        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
        'safe': 'active',  # ensures safe search is ON
        'imgType': 'photo',  # photo for actual images
    }

    gis.search(search_params=_search_params)

    images_info = []  # List to hold info for collage creation
    for image in gis.results():
        image.download(download_path)
        image.resize(500, 500)
        # appends image info
        images_info.append([image.path, 0, 0, 500, 500])

    return images_info


def create_collage(images_info):
    collage_width = max(img[1] + img[3] for img in images_info)
    collage_height = max(img[2] + img[4] for img in images_info)
    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))

    for img_info in images_info:
        img = Image.open(img_info[0])
        img = img.resize((img_info[3], img_info[4]))
        collage.paste(img, (img_info[1], img_info[2]))

    return collage


def save_collage(collage, file_path):
    collage.save(file_path)


if __name__ == "__main__":
    main()
