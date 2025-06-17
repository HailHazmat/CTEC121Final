import sys
import pytest
from unittest.mock import patch  # for overriding the global value
from PIL import Image
from project import get_canvasSize, create_collage, save_collage
import os
import project
project.set_num_results(4)

# Make sure sys.argv has at least 3 elements
while len(sys.argv) < 3:
    sys.argv.append('')

# safely set sys.argv[2]
sys.argv[2] = 4


@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "temp_output.png"


def test_get_canvasSize():
    # Set num_results to 4 (2x2 grid) and test canvas size
    expected_size = (1500, 1500)  # Considering each image is 500x500 with 250 padding
    assert get_canvasSize() == expected_size, f"Expected {expected_size}, got {get_canvasSize()} for num_results=4"


def test_create_collage():
    images_info = [
        ['images/dummy_img1.png', 0, 0, 500, 500],
        ['images/dummy_img2.png', 0, 0, 500, 500],
        ['images/dummy_img3.png', 0, 0, 500, 500],
        ['images/dummy_img4.jpg', 0, 0, 500, 500],
    ]
    canvas = (1000, 1000)  # since we know the image amount, this is set
    collage = create_collage(images_info, canvas)
    assert isinstance(collage, Image.Image)


def test_save_collage(temp_file):
    collage = Image.new('RGB', (500, 500), (255, 255, 255))
    save_collage(collage, str(temp_file))
    assert temp_file.exists()
